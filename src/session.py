"""
TermMux-CLI 会话管理模块
Session Management Module
"""

import json
from pathlib import Path
from typing import List, Optional
from datetime import datetime

from .workspace import WorkspaceManager


class SessionManager:
    """
    会话管理器
    Session Manager
    """

    def __init__(self, config):
        self.config = config
        self.config.ensure_dirs()

    def save_session(self, name: str, workspace_manager: WorkspaceManager):
        """保存会话"""
        session_data = workspace_manager.to_dict()
        session_data["saved_at"] = datetime.now().isoformat()
        session_data["name"] = name

        session_file = self.config.get_session_path(name)
        with open(session_file, "w", encoding="utf-8") as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)

    def load_session(self, name: str, workspace_manager: WorkspaceManager) -> bool:
        """加载会话"""
        session_file = self.config.get_session_path(name)
        if not session_file.exists():
            return False

        try:
            with open(session_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            loaded_manager = WorkspaceManager.from_dict(data, self.config)
            workspace_manager.workspaces = loaded_manager.workspaces
            workspace_manager.active_workspace_index = loaded_manager.active_workspace_index
            return True
        except (json.JSONDecodeError, KeyError):
            return False

    def delete_session(self, name: str) -> bool:
        """删除会话"""
        session_file = self.config.get_session_path(name)
        if session_file.exists():
            session_file.unlink()
            return True
        return False

    def list_sessions(self) -> List[str]:
        """列出所有会话"""
        sessions_dir = self.config.get_sessions_dir()
        if not sessions_dir.exists():
            return []

        sessions = []
        for file in sessions_dir.glob("*.json"):
            sessions.append(file.stem)
        return sorted(sessions)

    def get_session_info(self, name: str) -> Optional[dict]:
        """获取会话信息"""
        session_file = self.config.get_session_path(name)
        if not session_file.exists():
            return None

        try:
            with open(session_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {
                "name": data.get("name", name),
                "saved_at": data.get("saved_at", ""),
                "workspace_count": len(data.get("workspaces", [])),
            }
        except json.JSONDecodeError:
            return None

    def rename_session(self, old_name: str, new_name: str) -> bool:
        """重命名会话"""
        old_file = self.config.get_session_path(old_name)
        new_file = self.config.get_session_path(new_name)

        if old_file.exists() and not new_file.exists():
            old_file.rename(new_file)
            return True
        return False
