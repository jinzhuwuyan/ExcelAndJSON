#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "ui_mainwindow.h"

namespace Ui {
	class TableToolsWindow : public MainWindow
	{
		Q_OBJECT

	public:
		explicit TableToolsWindow(QWidget *parent = 0);
		~TableToolsWindow();

	private:
		Ui::MainWindow *ui;

	};
}



#endif // MAINWINDOW_H
