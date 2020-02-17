#include "mainwindow.h"

namespace Ui
{
	TableToolsWindow* tableInstance = nullptr;

	TableToolsWindow* GetSingleton()
	{
		if (tableInstance == nullptr)
		{
			tableInstance = new TableToolsWindow(nullptr);
		}
		return tableInstance;
	}

	TableToolsWindow::TableToolsWindow(QWidget *parent /*= 0*/) : MainWindow()
	{

	}

	TableToolsWindow::~TableToolsWindow()
	{

	}

}

