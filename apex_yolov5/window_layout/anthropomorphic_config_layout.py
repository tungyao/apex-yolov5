from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout


class AnthropomorphicConfigLayout:
    def __init__(self, config, main_window, parent_layout):
        self.config = config
        self.main_window = main_window
        self.parent_layout = parent_layout

    def add_layout(self):
        self.label = QLabel("鼠标拟人化设置")
        self.label.setAlignment(Qt.AlignCenter)
        intention_deviation_layout = QVBoxLayout()
        intention_deviation_layout.setObjectName("intention_deviation_layout")
        self.intention_deviation_toggle = QCheckBox("是否启动漏枪（根据配置周期性停止瞄准）")
        self.intention_deviation_toggle.setObjectName("intention_deviation_toggle")

        intention_deviation_interval_layout = QHBoxLayout()
        self.intention_deviation_interval_label = QLabel("漏枪周期")
        self.intention_deviation_interval = QLineEdit(self.main_window)
        self.intention_deviation_interval.setValidator(QIntValidator())
        intention_deviation_interval_layout.addWidget(self.intention_deviation_interval_label)
        intention_deviation_interval_layout.addWidget(self.intention_deviation_interval)
        self.intention_deviation_duration_label = QLabel("持续次数")
        self.intention_deviation_duration = QLineEdit(self.main_window)
        self.intention_deviation_duration.setValidator(QIntValidator())
        intention_deviation_interval_layout.addWidget(self.intention_deviation_duration_label)
        intention_deviation_interval_layout.addWidget(self.intention_deviation_duration)

        self.intention_deviation_force = QCheckBox("强制漏枪（将停止瞄准改变为强制将移动到人物外）")
        self.intention_deviation_force.setObjectName("intention_deviation_force")
        intention_deviation_layout.addWidget(self.intention_deviation_toggle)
        intention_deviation_layout.addLayout(intention_deviation_interval_layout)
        intention_deviation_layout.addWidget(self.intention_deviation_force)

        random_aim_layout = QVBoxLayout()
        random_aim_layout.setObjectName("random_aim_layout")
        self.random_aim_toggle = QCheckBox("随机弹道（准星在人物一定范围内按频率更换瞄准点）")
        self.random_aim_toggle.setObjectName("random_aim_toggle")

        random_coefficient_layout = QHBoxLayout()
        self.random_coefficient_label = QLabel("随机范围（0到1的小数）")
        self.random_coefficient = QLineEdit(self.main_window)
        self.random_coefficient.setValidator(QDoubleValidator())

        self.random_change_frequency_label = QLabel("瞄准点更换周期")
        self.random_change_frequency = QLineEdit(self.main_window)
        self.random_change_frequency.setValidator(QDoubleValidator())
        random_coefficient_layout.addWidget(self.random_coefficient_label)
        random_coefficient_layout.addWidget(self.random_coefficient)
        random_coefficient_layout.addWidget(self.random_change_frequency_label)
        random_coefficient_layout.addWidget(self.random_change_frequency)

        random_aim_layout.addWidget(self.random_aim_toggle)
        random_aim_layout.addLayout(random_coefficient_layout)

        lead_time_layout = QHBoxLayout()
        self.lead_time_toggle = QCheckBox("开启提前量（测试中）")
        self.lead_time_toggle.setObjectName("lead_time_toggle")
        self.lead_time_toggle.toggled.connect(self.lead_time_toggle_check)
        self.lead_time_frame_label = QLabel("提前帧")
        self.lead_time_frame_input = QLineEdit(self.main_window)
        self.lead_time_frame_input.setValidator(QIntValidator())

        self.lead_time_decision_frame_label = QLabel("判定帧")
        self.lead_time_decision_frame_input = QLineEdit(self.main_window)
        self.lead_time_decision_frame_input.setValidator(QIntValidator())

        lead_time_layout.addWidget(self.lead_time_frame_label)
        lead_time_layout.addWidget(self.lead_time_frame_input)
        lead_time_layout.addWidget(self.lead_time_decision_frame_label)
        lead_time_layout.addWidget(self.lead_time_decision_frame_input)

        delayed_aiming_layout = QVBoxLayout()
        self.delayed_aiming = QCheckBox("瞄准死区")
        delayed_aiming_xy_layout = QHBoxLayout()
        self.delayed_aiming.setObjectName("delayed_aiming")
        self.delayed_aiming.toggled.connect(self.delayed_aiming_toggle_check)
        self.delayed_aiming_factor_x_label = QLabel("死区范围(x)")
        self.delayed_aiming_factor_x_input = QLineEdit(self.main_window)
        self.delayed_aiming_factor_x_input.setValidator(QDoubleValidator())
        self.delayed_aiming_factor_y_label = QLabel("死区范围(y)")
        self.delayed_aiming_factor_y_input = QLineEdit(self.main_window)
        self.delayed_aiming_factor_y_input.setValidator(QDoubleValidator())
        delayed_aiming_xy_layout.addWidget(self.delayed_aiming_factor_x_label)
        delayed_aiming_xy_layout.addWidget(self.delayed_aiming_factor_x_input)
        delayed_aiming_xy_layout.addWidget(self.delayed_aiming_factor_y_label)
        delayed_aiming_xy_layout.addWidget(self.delayed_aiming_factor_y_input)
        delayed_aiming_layout.addWidget(self.delayed_aiming)
        delayed_aiming_layout.addLayout(delayed_aiming_xy_layout)

        self.parent_layout.addWidget(self.label)
        self.parent_layout.addLayout(intention_deviation_layout)
        self.parent_layout.addLayout(random_aim_layout)
        self.parent_layout.addLayout(delayed_aiming_layout)
        self.parent_layout.addWidget(self.lead_time_toggle)
        self.parent_layout.addLayout(lead_time_layout)

        self.init_form_config()

    def lead_time_toggle_check(self, checked):
        self.lead_time_frame_label.setVisible(checked)
        self.lead_time_frame_input.setVisible(checked)
        self.lead_time_decision_frame_label.setVisible(checked)
        self.lead_time_decision_frame_input.setVisible(checked)

    def delayed_aiming_toggle_check(self, checked):
        self.delayed_aiming_factor_x_label.setVisible(checked)
        self.delayed_aiming_factor_x_input.setVisible(checked)
        self.delayed_aiming_factor_y_label.setVisible(checked)
        self.delayed_aiming_factor_y_input.setVisible(checked)

    def init_form_config(self):
        self.intention_deviation_toggle.setChecked(self.config.intention_deviation_toggle)
        self.intention_deviation_interval.setText(str(self.config.intention_deviation_interval))
        self.intention_deviation_duration.setText(str(self.config.intention_deviation_duration))
        self.intention_deviation_force.setChecked(self.config.intention_deviation_force)

        self.random_aim_toggle.setChecked(self.config.random_aim_toggle)
        self.random_coefficient.setText(str(self.config.random_coefficient))
        self.random_change_frequency.setText(str(self.config.random_change_frequency))
        self.lead_time_toggle.setChecked(self.config.lead_time_toggle)
        self.lead_time_frame_input.setText(str(self.config.lead_time_frame))
        self.lead_time_decision_frame_input.setText(str(self.config.lead_time_decision_frame))
        self.lead_time_toggle_check(self.config.lead_time_toggle)

        self.delayed_aiming.setChecked(self.config.delayed_aiming)
        self.delayed_aiming_factor_x_input.setText(str(self.config.delayed_aiming_factor_x))
        self.delayed_aiming_factor_y_input.setText(str(self.config.delayed_aiming_factor_y))

    def save_config(self):
        self.config.set_config("intention_deviation_toggle", self.intention_deviation_toggle.isChecked())
        self.config.set_config("intention_deviation_interval", int(self.intention_deviation_interval.text()))
        self.config.set_config("intention_deviation_duration", int(self.intention_deviation_duration.text()))
        self.config.set_config("intention_deviation_force", self.intention_deviation_force.isChecked())

        self.config.set_config("random_aim_toggle", self.random_aim_toggle.isChecked())
        self.config.set_config("random_coefficient", float(self.random_coefficient.text()))
        self.config.set_config("random_change_frequency", int(self.random_change_frequency.text()))
        self.config.set_config("lead_time_toggle", self.lead_time_toggle.isChecked())
        self.config.set_config("lead_time_frame", int(self.lead_time_frame_input.text()))
        self.config.set_config("lead_time_decision_frame", int(self.lead_time_decision_frame_input.text()))

        self.config.set_config("delayed_aiming", self.delayed_aiming.isChecked())
        self.config.set_config("delayed_aiming_factor_x", float(self.delayed_aiming_factor_x_input.text()))
        self.config.set_config("delayed_aiming_factor_y", float(self.delayed_aiming_factor_y_input.text()))
