"""启动器关于页面：仅显示本地版本信息。"""
import tkinter as tk

from launcher.gui_theme import COLORS
from launcher.version import CURRENT_VERSION


def render_about_page(app):
    """在右侧内容区显示项目名称和当前版本。"""
    content = app._content_frame
    tk.Label(content, text="关于", font=("微软雅黑", 14, "bold"),
             fg=COLORS["text"], bg=COLORS["card_bg"]).pack(
        anchor=tk.W, padx=20, pady=(16, 8))
    tk.Label(content, text="闲鱼自动回复管理系统",
             font=("微软雅黑", 12), fg=COLORS["text"],
             bg=COLORS["card_bg"]).pack(anchor=tk.W, padx=20)
    tk.Label(content, text=f"当前版本: v{CURRENT_VERSION}",
             font=("微软雅黑", 10), fg=COLORS["text_secondary"],
             bg=COLORS["card_bg"]).pack(anchor=tk.W, padx=20, pady=(0, 8))
