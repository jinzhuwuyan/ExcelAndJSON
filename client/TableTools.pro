#-------------------------------------------------
#
# Project created by QtCreator 2020-02-04T15:39:12
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = TableTools
TEMPLATE = app

SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h \
    ui_mainwindow.h

FORMS    += mainwindow.ui

QMAKE_MAC_SDK = macosx10.14
