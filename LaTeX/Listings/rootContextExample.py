from src.controller.invController import invController
from PySide6.QtQml import QQmlApplicationEngine

engine = QQmlApplicationEngine()
invController = invController()
engine.rootContext().setContextProperty("iC", invController)