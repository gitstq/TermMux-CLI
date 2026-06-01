"""
TermMux-CLI 窗格管理模块
Pane Management Module
"""

import uuid
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


class SplitDirection(Enum):
    """分屏方向"""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


@dataclass
class Pane:
    """
    窗格对象
    Pane Object
    """

    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    title: str = "新窗格"
    command: Optional[str] = None
    working_directory: str = ""
    split_direction: SplitDirection = SplitDirection.VERTICAL
    width: int = 80
    height: int = 24
    is_active: bool = True

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "id": self.id,
            "title": self.title,
            "command": self.command,
            "working_directory": self.working_directory,
            "split_direction": self.split_direction.value,
            "width": self.width,
            "height": self.height,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Pane":
        """从字典创建"""
        return cls(
            id=data.get("id", str(uuid.uuid4())[:8]),
            title=data.get("title", "新窗格"),
            command=data.get("command"),
            working_directory=data.get("working_directory", ""),
            split_direction=SplitDirection(data.get("split_direction", "vertical")),
            width=data.get("width", 80),
            height=data.get("height", 24),
            is_active=data.get("is_active", True),
        )


class PaneManager:
    """
    窗格管理器
    Pane Manager
    """

    def __init__(self):
        self.panes: List[Pane] = []

    def create_pane(
        self,
        title: str = "新窗格",
        command: Optional[str] = None,
        working_directory: str = "",
        split_direction: SplitDirection = SplitDirection.VERTICAL,
    ) -> Pane:
        """创建新窗格"""
        pane = Pane(
            title=title,
            command=command,
            working_directory=working_directory,
            split_direction=split_direction,
        )
        self.panes.append(pane)
        return pane

    def split_pane(
        self,
        pane_id: str,
        direction: SplitDirection = SplitDirection.HORIZONTAL,
    ) -> Optional[Pane]:
        """分割窗格"""
        for i, pane in enumerate(self.panes):
            if pane.id == pane_id:
                new_pane = Pane(
                    title=f"{pane.title} (复制)",
                    working_directory=pane.working_directory,
                    split_direction=direction,
                    width=pane.width // 2 if direction == SplitDirection.VERTICAL else pane.width,
                    height=pane.height // 2 if direction == SplitDirection.HORIZONTAL else pane.height,
                )
                self.panes.insert(i + 1, new_pane)
                return new_pane
        return None

    def close_pane(self, pane_id: str) -> bool:
        """关闭窗格"""
        if len(self.panes) > 1:
            self.panes = [p for p in self.panes if p.id != pane_id]
            return True
        return False

    def get_pane(self, pane_id: str) -> Optional[Pane]:
        """获取窗格"""
        for pane in self.panes:
            if pane.id == pane_id:
                return pane
        return None

    def resize_pane(self, pane_id: str, width: int, height: int):
        """调整窗格大小"""
        pane = self.get_pane(pane_id)
        if pane:
            pane.width = width
            pane.height = height

    def to_dict(self) -> dict:
        """转换为字典"""
        return {"panes": [p.to_dict() for p in self.panes]}

    @classmethod
    def from_dict(cls, data: dict) -> "PaneManager":
        """从字典创建"""
        manager = cls()
        manager.panes = [Pane.from_dict(p) for p in data.get("panes", [])]
        return manager
