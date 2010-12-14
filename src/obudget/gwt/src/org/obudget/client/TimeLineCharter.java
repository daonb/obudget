package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.user.client.ui.LayoutPanel;
import com.google.gwt.user.client.ui.Panel;
import com.google.gwt.visualization.client.DataTable;
import com.google.gwt.visualization.client.AbstractDataTable.ColumnType;
import com.google.gwt.visualization.client.visualizations.AreaChart;

class TimeLineCharter extends Composite {
	private Panel mPanel;
	private Application mApp;

	public TimeLineCharter( Application app ) {
		mApp = app;
		mPanel = new LayoutPanel();
		initWidget(mPanel);
	}
	
	public void handleData( LinkedList<BudgetLine> list ) {
		if ( list.size() == 0 ) { return; }

		AreaChart.Options options = AreaChart.Options.create();
		options.setWidth(600);
		options.setHeight(280);
		options.setTitle( list.get(0).getTitle() + " - " + "הקצאה באלפי \u20AA, מותאם לאינפלציה" );
		options.setTitleX("שנה");
		options.setTitleY("תקציב באלפי \u20AA");
		
		DataTable data = DataTable.create();
	    data.addColumn(ColumnType.STRING, "Year");
	    data.addColumn(ColumnType.NUMBER, "הקצאת תקציב" );
	    data.addColumn(ColumnType.NUMBER, "הקצאה מעודכנת" );
	    data.addColumn(ColumnType.NUMBER, "שימוש בפועל" );
	    data.addRows(list.size());
	    for ( int i = 0 ; i < list.size() ; i ++ ) {
		    data.setValue(list.size()-i-1, 0, list.get(i).getYear().toString() );
		    data.setValue(list.size()-i-1, 1, list.get(i).getInfAllocated() );
		    data.setValue(list.size()-i-1, 2, list.get(i).getInfRevised());
		    data.setValue(list.size()-i-1, 3, list.get(i).getInfUsed() );
	    }
		AreaChart areachart = new AreaChart( data, options );
		mPanel.add(areachart);
	}
}
