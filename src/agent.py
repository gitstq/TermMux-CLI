"""
TermMux-CLI AI Agent检测模块
AI Agent Detection Module
"""

import os
import re
import psutil
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

from .config import Config


class AgentStatus(Enum):
    """Agent状态"""

    IDLE = "idle"
    WORKING = "working"
    BLOCKED = "blocked"
    DONE = "done"


@dataclass
class DetectedAgent:
    """检测到的Agent"""

    name: str
    pid: int
    status: AgentStatus
    command: str
    working_directory: str = ""
    process: Optional[psutil.Process] = None

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "name": self.name,
            "pid": self.pid,
            "status": self.status.value,
            "command": self.command,
            "working_directory": self.working_directory,
        }


class AgentDetector:
    """
    AI Agent检测器
    AI Agent Detector

    支持检测的Agent:
    - Claude Code
    - Cursor Agent
    - GitHub Copilot CLI
    - OpenAI Codex
    - Gemini CLI
    - Kiro CLI
    """

    # Agent特征定义
    AGENT_PATTERNS = {
        "claude": {
            "process_names": ["claude", "claude-code"],
            "command_patterns": [r"claude", r"claude-code", r"/\.claude/"],
            "status_keywords": {
                AgentStatus.WORKING: ["Thinking...", "Writing...", "Executing...", "Searching..."],
                AgentStatus.BLOCKED: ["awaiting", "approval", "confirm", "blocked"],
                AgentStatus.DONE: ["done", "complete", "finished"],
            },
        },
        "cursor": {
            "process_names": ["cursor", "cursor-agent"],
            "command_patterns": [r"cursor", r"--agent"],
            "status_keywords": {
                AgentStatus.WORKING: ["Working", "Implementing", "Running"],
                AgentStatus.BLOCKED: ["waiting", "input"],
                AgentStatus.DONE: ["Done", "Complete"],
            },
        },
        "copilot": {
            "process_names": ["github-copilot", "copilot-cli"],
            "command_patterns": [r"gh cp", r"github-copilot", r"copilot"],
            "status_keywords": {
                AgentStatus.WORKING: ["processing", "generating"],
                AgentStatus.BLOCKED: ["need"],
                AgentStatus.DONE: ["done"],
            },
        },
        "codex": {
            "process_names": ["codex", "openai-codex"],
            "command_patterns": [r"codex", r"openai-codex"],
            "status_keywords": {
                AgentStatus.WORKING: ["running", "executing"],
                AgentStatus.BLOCKED: ["waiting"],
                AgentStatus.DONE: ["complete"],
            },
        },
        "gemini": {
            "process_names": ["gemini", "google-gemini"],
            "command_patterns": [r"gemini", r"google-gemini"],
            "status_keywords": {
                AgentStatus.WORKING: ["thinking", "processing"],
                AgentStatus.BLOCKED: ["input needed"],
                AgentStatus.DONE: ["finished"],
            },
        },
        "kiro": {
            "process_names": ["kiro", "kiro-cli"],
            "command_patterns": [r"kiro"],
            "status_keywords": {
                AgentStatus.WORKING: ["working"],
                AgentStatus.BLOCKED: ["waiting"],
                AgentStatus.DONE: ["done"],
            },
        },
    }

    def __init__(self, config: Optional[Config] = None):
        self.config = config
        self.detected_agents: List[DetectedAgent] = []
        self._process_cache: Dict[int, Dict] = {}

    def scan(self) -> List[DetectedAgent]:
        """
        扫描并检测运行中的AI Agent
        Scan and detect running AI Agents
        """
        self.detected_agents = []

        try:
            for proc in psutil.process_iter(["pid", "name", "cmdline", "cwd"]):
                try:
                    agent_info = self._check_process(proc)
                    if agent_info:
                        self.detected_agents.append(agent_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except Exception:
            pass

        return self.detected_agents

    def _check_process(self, proc: psutil.Process) -> Optional[DetectedAgent]:
        """检查进程是否为AI Agent"""
        try:
            process_name = proc.name().lower()
            cmdline = " ".join(proc.cmdline()).lower() if proc.cmdline() else ""
            cwd = proc.cwd() or ""

            for agent_type, patterns in self.AGENT_PATTERNS.items():
                # 检查进程名
                if any(name in process_name for name in patterns["process_names"]):
                    agent_name = self._get_agent_display_name(agent_type)
                    status = self._detect_agent_status(proc, patterns)

                    return DetectedAgent(
                        name=agent_name,
                        pid=proc.pid,
                        status=status,
                        command=cmdline,
                        working_directory=cwd,
                        process=proc,
                    )

                # 检查命令行
                for pattern in patterns["command_patterns"]:
                    if re.search(pattern, cmdline, re.IGNORECASE):
                        agent_name = self._get_agent_display_name(agent_type)
                        status = self._detect_agent_status(proc, patterns)

                        return DetectedAgent(
                            name=agent_name,
                            pid=proc.pid,
                            status=status,
                            command=cmdline,
                            working_directory=cwd,
                            process=proc,
                        )

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

        return None

    def _detect_agent_status(self, proc: psutil.Process, patterns: dict) -> AgentStatus:
        """检测Agent状态"""
        try:
            # 检查终端输出（如果有）
            status_keywords = patterns.get("status_keywords", {})

            # 尝试从环境变量或状态文件获取状态
            # 这里简化处理，默认为WORKING
            return AgentStatus.WORKING
        except Exception:
            return AgentStatus.IDLE

    def _get_agent_display_name(self, agent_type: str) -> str:
        """获取Agent显示名称"""
        names = {
            "claude": "Claude Code",
            "cursor": "Cursor Agent",
            "copilot": "GitHub Copilot",
            "codex": "OpenAI Codex",
            "gemini": "Gemini CLI",
            "kiro": "Kiro CLI",
        }
        return names.get(agent_type, agent_type.title())

    def get_detected_agents(self) -> List[DetectedAgent]:
        """获取检测到的Agent列表"""
        return self.detected_agents

    def get_agents_by_status(self, status: AgentStatus) -> List[DetectedAgent]:
        """按状态获取Agent"""
        return [a for a in self.detected_agents if a.status == status]

    def get_agent_summary(self) -> Dict[str, int]:
        """获取Agent状态摘要"""
        summary = {status.value: 0 for status in AgentStatus}
        for agent in self.detected_agents:
            summary[agent.status.value] += 1
        return summary

    def terminate_agent(self, pid: int) -> bool:
        """终止Agent进程"""
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
