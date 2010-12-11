package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.user.client.ui.LayoutPanel;
import com.google.gwt.user.client.ui.Panel;
import com.google.gwt.visualization.client.DataTable;
import com.google.gwt.visualization.client.AbstractDataTable.ColumnType;
import com.google.gwt.visualization.client.visualizations.PieChart;
import com.google.gwt.visualization.client.visualizations.PieChart.Options;

class PieCharter extends Composite {
	private Panel mPanel;
	private Application mApp;

	public PieCharter( Application app ) {
		mApp = app;
		mPanel = new LayoutPanel();
		initWidget(mPanel);
	}
	
	public void handleData( LinkedList<BudgetLine> list ) {
		if ( list.size() < 2 ) { return; }

		Options	options = Options.create();
		options.setWidth(600);
		options.setHeight(260);
		options.set3D(true);
		options.setTitle(list.get(0).getTitle());

	    DataTable data = DataTable.create();
	    data.addColumn(ColumnType.STRING, "Title");
	    data.addColumn(ColumnType.NUMBER, "Allocated");
	    data.addRows(list.size()-1);
	    for ( int i = 0 ; i < list.size()-1 ; i ++ ) {
		    data.setValue(i, 0, list.get(i+1).getTitle());
		    data.setValue(i, 1, list.get(i+1).getAllocated());
	    }
		PieChart piechart = new PieChart( data, options );
		mPanel.add(piechart);
	}
}
