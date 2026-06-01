"""
TermMux-CLI 核心模块
Core module for TermMux-CLI
"""

import os
import sys
import json
import asyncio
from pathlib import Path
from typing import Optional, Dict, List
from dataclasses import dataclass, field

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table

from .workspace import WorkspaceManager
from .pane import PaneManager
from .agent import AgentDetector, AgentStatus
from .session import SessionManager
from .config import Config


@dataclass
class TermMux:
    """
    TermMux 主控制器
    Main controller for TermMux
    """

    config: Config = field(default_factory=Config)
    console: Console = field(default_factory=Console)
    workspace_manager: WorkspaceManager = field(default_factory=WorkspaceManager)
    pane_manager: PaneManager = field(default_factory=PaneManager)
    agent_detector: AgentDetector = field(default_factory=AgentDetector)
    session_manager: SessionManager = field(default_factory=SessionManager)

    def __post_init__(self):
        """初始化组件"""
        self.workspace_manager = WorkspaceManager(self.config)
        self.pane_manager = PaneManager()
        self.agent_detector = AgentDetector()
        self.session_manager = SessionManager(self.config)

    def create_layout(self) -> Layout:
        """创建主界面布局"""
        layout = Layout()

        # 顶部状态栏
        top_panel = Panel(
            "[bold cyan]TermMux-CLI[/bold cyan] | "
            f"工作区: {len(self.workspace_manager.workspaces)} | "
            f"Agent检测: {len(self.agent_detector.detected_agents)} 个活动",
            style="bold blue",
        )

        # 主内容区
        main_content = self._build_workspace_view()

        # 底部信息栏
        bottom_panel = Panel(
            "[dim]Ctrl+B: 命令前缀 | Ctrl+C: 退出 | Tab: 切换工作区[/dim]",
            style="dim",
        )

        layout.split_column(
            Layout(top_panel, size=3),
            Layout(main_content, name="main"),
            Layout(bottom_panel, size=3),
        )

        return layout

    def _build_workspace_view(self) -> "Panel":
        """构建工作区视图"""
        table = Table(title="🎯 工作区管理 / Workspace Management", show_header=True)
        table.add_column("ID", style="cyan", width=6)
        table.add_column("名称", style="green", width=20)
        table.add_column("Agent状态", style="yellow", width=30)
        table.add_column("窗格数", style="magenta", width=8)

        for i, ws in enumerate(self.workspace_manager.workspaces):
            agent_status = self._get_agent_status_text(ws)
            table.add_row(
                str(i + 1),
                ws.name,
                agent_status,
                str(len(ws.panes)),
            )

        return Panel(table, title="📁 工作区")

    def _get_agent_status_text(self, workspace) -> str:
        """获取工作区的Agent状态文本"""
        if not workspace.agents:
            return "🟢 空闲"
        statuses = []
        for agent_name, status in workspace.agents.items():
            icon = self._get_agent_status_icon(status)
            statuses.append(f"{icon} {agent_name}")
        return " | ".join(statuses) if statuses else "🟢 空闲"

    def _get_agent_status_icon(self, status: AgentStatus) -> str:
        """获取状态图标"""
        icons = {
            AgentStatus.IDLE: "🟢",
            AgentStatus.WORKING: "🟡",
            AgentStatus.BLOCKED: "🔴",
            AgentStatus.DONE: "🔵",
        }
        return icons.get(status, "⚪")

    def run_interactive(self):
        """运行交互模式"""
        self.console.clear()
        self.console.print(
            Panel.fit(
                "[bold cyan]🎛️  TermMux-CLI[/bold cyan]\n"
                "[dim]轻量级终端多路复用与AI Agent感知管理器[/dim]\n\n"
                "[green]初始化完成，按键说明:[/green]\n"
                "  [cyan]n[/cyan] - 新建工作区\n"
                "  [cyan]s[/cyan] - 保存会话\n"
                "  [cyan]l[/cyan] - 加载会话\n"
                "  [cyan]r[/cyan] - 刷新Agent检测\n"
                "  [cyan]q[/cyan] - 退出",
                title="欢迎 / Welcome",
                border_style="blue",
            )
        )

        # 刷新Agent检测
        self.agent_detector.scan()

        # 显示检测到的Agent
        self._show_detected_agents()

        # 创建默认工作区
        if not self.workspace_manager.workspaces:
            self.workspace_manager.create_workspace("默认工作区")

        # 进入主循环
        self._main_loop()

    def _show_detected_agents(self):
        """显示检测到的Agent"""
        agents = self.agent_detector.get_detected_agents()
        if agents:
            table = Table(title="🤖 检测到的AI Agent", show_header=True)
            table.add_column("Agent名称", style="cyan")
            table.add_column("状态", style="yellow")
            table.add_column("PID", style="magenta")
            table.add_column("命令", style="green")

            for agent in agents:
                icon = self._get_agent_status_icon(agent.status)
                cmd_short = agent.command[:40] + "..." if len(agent.command) > 40 else agent.command
                table.add_row(agent.name, f"{icon} {agent.status.value}", str(agent.pid), cmd_short)

            self.console.print(table)
        else:
            self.console.print("[dim]未检测到AI Agent运行中[/dim]")

    def _main_loop(self):
        """主循环"""
        try:
            while True:
                self.console.print("\n[cyan]选择一个操作 (n/s/l/r/q):[/cyan] ", end="")
                choice = input().strip().lower()

                if choice == "n":
                    self._create_new_workspace()
                elif choice == "s":
                    self._save_session()
                elif choice == "l":
                    self._load_session()
                elif choice == "r":
                    self._refresh_agents()
                elif choice == "q":
                    self.console.print("[yellow]再见！/ Goodbye![/yellow]")
                    break
                else:
                    self.console.print("[red]无效选择 / Invalid choice[/red]")
        except KeyboardInterrupt:
            self.console.print("\n[yellow]已退出 / Exited[/yellow]")

    def _create_new_workspace(self):
        """创建新工作区"""
        self.console.print("输入工作区名称 / Enter workspace name: ", end="")
        name = input().strip()
        if name:
            self.workspace_manager.create_workspace(name)
            self.console.print(f"[green]✓ 工作区 '{name}' 已创建[/green]")
        else:
            self.console.print("[red]✗ 名称不能为空[/red]")

    def _save_session(self):
        """保存会话"""
        self.console.print("输入会话名称 / Enter session name: ", end="")
        name = input().strip()
        if name:
            self.session_manager.save_session(name, self.workspace_manager)
            self.console.print(f"[green]✓ 会话 '{name}' 已保存[/green]")
        else:
            self.console.print("[red]✗ 名称不能为空[/red]")

    def _load_session(self):
        """加载会话"""
        sessions = self.session_manager.list_sessions()
        if not sessions:
            self.console.print("[yellow]没有已保存的会话 / No saved sessions[/yellow]")
            return

        self.console.print("[cyan]可用的会话:[/cyan]")
        for i, name in enumerate(sessions, 1):
            self.console.print(f"  {i}. {name}")

        self.console.print("选择会话编号 / Select session number: ", end="")
        try:
            idx = int(input().strip()) - 1
            if 0 <= idx < len(sessions):
                self.session_manager.load_session(sessions[idx], self.workspace_manager)
                self.console.print(f"[green]✓ 会话 '{sessions[idx]}' 已加载[/green]")
            else:
                self.console.print("[red]✗ 无效编号 / Invalid number[/red]")
        except ValueError:
            self.console.print("[red]✗ 请输入有效数字 / Please enter a valid number[/red]")

    def _refresh_agents(self):
        """刷新Agent检测"""
        self.agent_detector.scan()
        self._show_detected_agents()


def main():
    """主入口函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="TermMux-CLI - 轻量级终端多路复用与AI Agent感知管理器"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--init", action="store_true", help="初始化配置")
    parser.add_argument("--list-sessions", action="store_true", help="列出已保存的会话")
    parser.add_argument("--config-dir", help="指定配置目录")

    args = parser.parse_args()

    # 创建实例并运行
    mux = TermMux()
    mux.run_interactive()


if __name__ == "__main__":
    main()
