"""
TermMux-CLI 工作区管理模块
Workspace Management Module
"""

import uuid
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

from .pane import Pane


@dataclass
class Workspace:
    """
    工作区对象
    Workspace Object
    """

    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str = "默认工作区"
    panes: List[Pane] = field(default_factory=list)
    agents: Dict[str, str] = field(default_factory=dict)  # agent_name -> status
    created_at: datetime = field(default_factory=datetime.now)
    active_pane_index: int = 0

    def add_pane(self, pane: Pane):
        """添加窗格"""
        self.panes.append(pane)
        self.active_pane_index = len(self.panes) - 1

    def remove_pane(self, pane_id: str):
        """移除窗格"""
        self.panes = [p for p in self.panes if p.id != pane_id]
        if self.active_pane_index >= len(self.panes):
            self.active_pane_index = max(0, len(self.panes) - 1)

    def get_active_pane(self) -> Optional[Pane]:
        """获取当前活动窗格"""
        if 0 <= self.active_pane_index < len(self.panes):
            return self.panes[self.active_pane_index]
        return None

    def focus_next_pane(self):
        """聚焦下一个窗格"""
        if self.panes:
            self.active_pane_index = (self.active_pane_index + 1) % len(self.panes)

    def focus_prev_pane(self):
        """聚焦上一个窗格"""
        if self.panes:
            self.active_pane_index = (self.active_pane_index - 1) % len(self.panes)

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "id": self.id,
            "name": self.name,
            "panes": [p.to_dict() for p in self.panes],
            "agents": self.agents,
            "created_at": self.created_at.isoformat(),
            "active_pane_index": self.active_pane_index,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Workspace":
        """从字典创建"""
        ws = cls(
            id=data.get("id", str(uuid.uuid4())[:8]),
            name=data.get("name", "默认工作区"),
            agents=data.get("agents", {}),
        )
        ws.panes = [Pane.from_dict(p) for p in data.get("panes", [])]
        ws.active_pane_index = data.get("active_pane_index", 0)
        return ws


class WorkspaceManager:
    """
    工作区管理器
    Workspace Manager
    """

    def __init__(self, config=None):
        self.config = config
        self.workspaces: List[Workspace] = []
        self.active_workspace_index: int = 0

    def create_workspace(self, name: str) -> Workspace:
        """创建新工作区"""
        workspace = Workspace(name=name)
        self.workspaces.append(workspace)
        self.active_workspace_index = len(self.workspaces) - 1
        return workspace

    def delete_workspace(self, workspace_id: str):
        """删除工作区"""
        self.workspaces = [w for w in self.workspaces if w.id != workspace_id]
        if self.active_workspace_index >= len(self.workspaces):
            self.active_workspace_index = max(0, len(self.workspaces) - 1)

    def get_active_workspace(self) -> Optional[Workspace]:
        """获取当前活动工作区"""
        if 0 <= self.active_workspace_index < len(self.workspaces):
            return self.workspaces[self.active_workspace_index]
        return None

    def switch_workspace(self, index: int):
        """切换工作区"""
        if 0 <= index < len(self.workspaces):
            self.active_workspace_index = index

    def rename_workspace(self, workspace_id: str, new_name: str):
        """重命名工作区"""
        for ws in self.workspaces:
            if ws.id == workspace_id:
                ws.name = new_name
                break

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "workspaces": [w.to_dict() for w in self.workspaces],
            "active_workspace_index": self.active_workspace_index,
        }

    @classmethod
    def from_dict(cls, data: dict, config=None) -> "WorkspaceManager":
        """从字典创建"""
        manager = cls(config=config)
        manager.workspaces = [Workspace.from_dict(w) for w in data.get("workspaces", [])]
        manager.active_workspace_index = data.get("active_workspace_index", 0)
        return manager
