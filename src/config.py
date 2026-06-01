"""
TermMux-CLI 配置管理模块
Configuration Management Module
"""

import os
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class Config:
    """
    TermMux 配置对象
    TermMux Configuration Object
    """

    config_dir: Path = field(default_factory=lambda: Path.home() / ".config" / "termmux")
    session_file: str = "sessions.json"
    history_file: str = "history.json"
    log_file: str = "termmux.log"

    # 界面配置
    theme: str = "default"
    show_status_bar: bool = True
    show_agent_indicators: bool = True

    # Agent检测配置
    scan_interval: int = 5  # 秒
    auto_detect_agents: bool = True

    # 会话配置
    auto_save: bool = False
    auto_save_interval: int = 300  # 秒

    # 快捷键配置
    prefix_key: str = "ctrl+b"

    def __post_init__(self):
        """确保配置目录存在"""
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def get_session_path(self, session_name: str) -> Path:
        """获取会话文件路径"""
        return self.config_dir / "sessions" / f"{session_name}.json"

    def get_sessions_dir(self) -> Path:
        """获取会话目录"""
        return self.config_dir / "sessions"

    def ensure_dirs(self):
        """确保所有必要的目录存在"""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.get_sessions_dir().mkdir(parents=True, exist_ok=True)

    def save(self):
        """保存配置到文件"""
        self.ensure_dirs()
        config_file = self.config_dir / "config.json"
        config_data = {
            "theme": self.theme,
            "show_status_bar": self.show_status_bar,
            "show_agent_indicators": self.show_agent_indicators,
            "scan_interval": self.scan_interval,
            "auto_detect_agents": self.auto_detect_agents,
            "auto_save": self.auto_save,
            "auto_save_interval": self.auto_save_interval,
            "prefix_key": self.prefix_key,
        }
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, config_dir: Optional[Path] = None) -> "Config":
        """从文件加载配置"""
        if config_dir is None:
            config_dir = Path.home() / ".config" / "termmux"

        config_file = config_dir / "config.json"
        if config_file.exists():
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                return cls(
                    config_dir=config_dir,
                    theme=data.get("theme", "default"),
                    show_status_bar=data.get("show_status_bar", True),
                    show_agent_indicators=data.get("show_agent_indicators", True),
                    scan_interval=data.get("scan_interval", 5),
                    auto_detect_agents=data.get("auto_detect_agents", True),
                    auto_save=data.get("auto_save", False),
                    auto_save_interval=data.get("auto_save_interval", 300),
                    prefix_key=data.get("prefix_key", "ctrl+b"),
                )
            except (json.JSONDecodeError, KeyError):
                pass

        return cls(config_dir=config_dir)

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "config_dir": str(self.config_dir),
            "theme": self.theme,
            "show_status_bar": self.show_status_bar,
            "show_agent_indicators": self.show_agent_indicators,
            "scan_interval": self.scan_interval,
            "auto_detect_agents": self.auto_detect_agents,
            "auto_save": self.auto_save,
            "auto_save_interval": self.auto_save_interval,
            "prefix_key": self.prefix_key,
        }
