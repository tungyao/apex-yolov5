from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QCheckBox, QHBoxLayout, QComboBox, QLineEdit

from apex_yolov5.KeyAndMouseListener import KMCallBack


class AiToggleLayout:
    def __init__(self, config, main_window, parent_layout, system_tray):
        self.config = config
        self.main_window = main_window
        self.parent_layout = parent_layout
        self.system_tray = system_tray
        KMCallBack.connect(
            KMCallBack(self.config.ai_toggle_type, self.config.ai_toggle_key, self.handle_middle_toggled))

    def add_layout(self):
        layout = QVBoxLayout()
        layout.setObjectName("Ai_toggle_layout")
        self.label = QLabel("启动设置")
        self.label.setAlignment(Qt.AlignCenter)
        toggle_layout = QHBoxLayout(self.main_window)
        self.ai_toggle_switch = QCheckBox("AI开关")
        self.ai_toggle_switch.setObjectName("ai_toggle")
        self.ai_toggle_switch.setChecked(self.config.ai_toggle)  # 初始化开关的值
        self.ai_toggle_switch.toggled.connect(self.handle_ai_toggled)
        toggle_layout.addWidget(self.ai_toggle_switch)

        # self.ai_middle_toggle_switch = QCheckBox("中键启停")
        # self.ai_middle_toggle_switch.setObjectName("ai_middle_toggle")
        # self.ai_middle_toggle_switch.setChecked(self.config.ai_middle_toggle)  # 初始化开关的值
        # self.ai_middle_toggle_switch.toggled.connect(self.handle_ai_middle_toggle_switch)
        # toggle_layout.addWidget(self.ai_middle_toggle_switch)

        # select_toggle_layout = QHBoxLayout(self.main_window)
        self.ai_toggle_type_label = QLabel("开关键配置")
        self.ai_toggle_type_combo_box = QComboBox()

        for key in self.config.ai_available_toggle_type:
            self.ai_toggle_type_combo_box.addItem(key)
        self.ai_toggle_type_combo_box.setCurrentText(self.config.ai_toggle_type)
        # self.ai_toggle_type_combo_box.currentIndexChanged.connect(self.selection_changed)

        self.toggle_key_edit = QLineEdit(self.main_window)
        self.toggle_key_edit.setText(self.config.ai_toggle_key)
        # self.toggle_key_edit.textChanged.connect(self.update_toggle_key)

        toggle_layout.addWidget(self.ai_toggle_type_label)
        toggle_layout.addWidget(self.ai_toggle_type_combo_box)
        toggle_layout.addWidget(self.toggle_key_edit)

        layout.addWidget(self.label)
        layout.addLayout(toggle_layout)
        # layout.addLayout(select_toggle_layout)

        self.parent_layout.addLayout(layout)

    def handle_ai_toggled(self, checked):
        self.config.set_config("ai_toggle", checked)

    def handle_ai_middle_toggle_switch(self, checked):
        self.config.set_config("ai_middle_toggle", checked)

    def handle_middle_toggled(self, pressed, toggle):
        self.ai_toggle_switch.setChecked(toggle)
        self.config.set_config("ai_toggle", toggle)
        self.config.ai_toggle = toggle
        self.system_tray.change_icon(toggle)

    def save_config(self):
        selected_key = self.ai_toggle_type_combo_box.currentText()
        KMCallBack.remove(self.config.ai_toggle_type, self.config.ai_toggle_key)
        self.config.set_config("ai_toggle_type", selected_key)
        self.config.set_config("ai_toggle_key", self.toggle_key_edit.text())
        KMCallBack.connect(
            KMCallBack(selected_key, self.toggle_key_edit.text(), self.handle_middle_toggled))