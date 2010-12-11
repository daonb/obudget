package org.obudget.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.event.dom.client.ChangeEvent;
import com.google.gwt.event.dom.client.ChangeHandler;
import com.google.gwt.event.logical.shared.SelectionEvent;
import com.google.gwt.event.logical.shared.SelectionHandler;
import com.google.gwt.user.client.History;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.SuggestBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.user.client.ui.SuggestOracle.Suggestion;
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
		 
		 final ListBox yearSelection = new ListBox();
		 yearSelection.addChangeHandler( new ChangeHandler() {
			
			@Override
			public void onChange(ChangeEvent event) {
				Integer index = yearSelection.getSelectedIndex();
				if ( index > 0 ) {
					mApp.selectYear( 1991+index );
				}				
			}
		});
		
		final SuggestBox suggest = new SuggestBox(new BudgetSuggestionOracle(yearSelection));
		suggest.setWidth("200px");
		suggest.addSelectionHandler( new SelectionHandler<Suggestion>() {
			@Override
			public void onSelection(SelectionEvent<Suggestion> event) {
				BudgetSuggestion bs = (BudgetSuggestion) event.getSelectedItem();
				History.newItem(bs.getCode() +","+ bs.getYear() );
			}
		});

		yearSelection.addItem("כולן");
		for ( Integer i = 1992 ; i<=2009 ; i ++ ) {
			yearSelection.addItem(i.toString());
		}

		HorizontalPanel hPanel = new HorizontalPanel();
		
		VerticalPanel filterPanel = new VerticalPanel();
		filterPanel.add(yearSelection);
		filterPanel.add(suggest);
		filterPanel.add(mApp.getResultsGrid());
		filterPanel.setWidth("400px");
		
		hPanel.add(filterPanel);
		
		VerticalPanel charts = new VerticalPanel();
		charts.add(mApp.getPieCharter());
		charts.add(mApp.getTimeLineCharter());
		hPanel.add(charts);
		hPanel.setHorizontalAlignment(HorizontalPanel.ALIGN_RIGHT);
		hPanel.setWidth("100%");
		RootPanel.get().add(hPanel);
		
		History.fireCurrentHistoryState();
	}
}
