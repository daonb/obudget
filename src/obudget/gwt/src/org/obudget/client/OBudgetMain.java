package org.obudget.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.core.client.GWT;
import com.google.gwt.resources.client.ClientBundle;
import com.google.gwt.resources.client.CssResource;
import com.google.gwt.user.client.History;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.visualization.client.VisualizationUtils;
import com.google.gwt.visualization.client.visualizations.AreaChart;
import com.google.gwt.visualization.client.visualizations.PieChart;

public class OBudgetMain implements EntryPoint {

	private Application mApp;
	
	public void onModuleLoad() {

		Runnable onLoadCallback = new Runnable() {
	        public void run() {
	        	init();
	        }
	      };

	    VisualizationUtils.loadVisualizationApi(onLoadCallback, PieChart.PACKAGE, AreaChart.PACKAGE );
	}

	private void init() {

		mApp = new Application();
		mApp.init(); 

		//filterPanel.add(mApp.getBreadcrumbs() );

		RootPanel.get("obudget-searchbox").add(mApp.getSearchBox());
		RootPanel.get("obudget-piechart").add(mApp.getPieCharter());
		RootPanel.get("obudget-timeline").add(mApp.getTimeLineCharter());
		RootPanel.get("obudget-summary-1").add(mApp.getSummary1() );
		RootPanel.get("obudget-breadcrumbs").add(mApp.getBreadcrumbs() );
		RootPanel.get("obudget-year-selection").add(mApp.getYearSelection() );
		RootPanel.get("obudget-summary-2").add(mApp.getSummary2() );
		RootPanel.get("obudget-summary-3").add(mApp.getSummary3() );
		RootPanel.get("obudget-detailed-results").add(mApp.getResultsGrid() );
		RootPanel.get("obudget-news").add(mApp.getBudgetNews() );

		History.fireCurrentHistoryState();
	}
}
