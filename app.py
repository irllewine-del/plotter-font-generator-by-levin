import os
import sys

import webview


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    webview.create_window(
        "Segoe Script Stroke — плоттер",
        resource_path("plotter.html"),
        width=1280,
        height=860,
        min_size=(800, 600),
    )
    webview.start()
