package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.dom.client.Style.Unit;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.user.client.ui.DecoratedTabPanel;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.LayoutPanel;
import com.google.gwt.user.client.ui.Panel;
import com.google.gwt.user.client.ui.RadioButton;
import com.google.gwt.user.client.ui.TabBar;
import com.google.gwt.user.client.ui.TabLayoutPanel;
import com.google.gwt.user.client.ui.ToggleButton;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.visualization.client.DataTable;
import com.google.gwt.visualization.client.LegendPosition;
import com.google.gwt.visualization.client.AbstractDataTable.ColumnType;
import com.google.gwt.visualization.client.visualizations.PieChart;
import com.google.gwt.visualization.client.visualizations.PieChart.Options;

class PieCharter extends Composite {
	private TabLayoutPanel mTabPanel;
	private VerticalPanel mPanel;
	private Application mApp;
	private RadioButton mRadio2;
	private ToggleButton mAllocatedButton;
	private ToggleButton mRevisedButton;
	private ToggleButton mUsedButton;
	private ToggleButton mNetButton;
	private LinkedList<BudgetLine> mList = null;

	public PieCharter( Application app ) {
		mApp = app;
		mTabPanel = new TabLayoutPanel(0,Unit.PX);
		mTabPanel.setHeight("305px");
		mTabPanel.setWidth("325px");
		mTabPanel.setStylePrimaryName("obudget-piechart");	
		
		mPanel = new VerticalPanel();
		mPanel.add(mTabPanel);
		
		HorizontalPanel hPanel = new HorizontalPanel();
		hPanel.setStylePrimaryName("obudget-piechart-type");
		mNetButton = new ToggleButton("נטו","ברוטו");
		mNetButton.addClickHandler( new ClickHandler() {			
			@Override
			public void onClick(ClickEvent event) {
				redrawChart();
			}
		});
		mAllocatedButton = new ToggleButton("הקצאה");
		mRevisedButton = new ToggleButton("הקצאה מעודכנת");
		mRevisedButton.setDown(true);
		mUsedButton = new ToggleButton("שימוש");
		mAllocatedButton.addClickHandler( new ClickHandler() {	
			@Override
			public void onClick(ClickEvent event) {
				if ( mAllocatedButton.isDown() ) {
					mTabPanel.selectTab(0);
					mRevisedButton.setDown(false);
					mUsedButton.setDown(false);
				} else {
					mAllocatedButton.setDown(true);
				}
				
			}
		});
		mRevisedButton.addClickHandler( new ClickHandler() {	
			@Override
			public void onClick(ClickEvent event) {
				if ( mRevisedButton.isDown() ) {
					mTabPanel.selectTab(1);
					mAllocatedButton.setDown(false);
					mUsedButton.setDown(false);
				} else {
					mRevisedButton.setDown(true);
				}
				
			}
		});
		mUsedButton.addClickHandler( new ClickHandler() {	
			@Override
			public void onClick(ClickEvent event) {
				if ( mUsedButton.isDown() ) {
					mTabPanel.selectTab(2);
					mAllocatedButton.setDown(false);
					mRevisedButton.setDown(false);
				} else {
					mUsedButton.setDown(true);
				}
				
			}
		});
		
		hPanel.add( mAllocatedButton );
		hPanel.add( mRevisedButton );
		hPanel.add( mUsedButton );
		hPanel.add( mNetButton );
		mPanel.add(hPanel);
		
		initWidget(mPanel);
	}
	
	public void handleData( LinkedList<BudgetLine> list ) {
		mList = list;
		redrawChart();
	}
	
	private void redrawChart() {
	    mTabPanel.clear();

	    if ( mList == null ) { return; }
	    if ( mList.size() < 2 ) { return; }

		Options	options = Options.create();
		options.setWidth(340);
		options.setHeight(305);
		options.set3D(true);	
		options.setLegend(LegendPosition.BOTTOM);

	    DataTable[] data = new DataTable[] { DataTable.create(), DataTable.create(), DataTable.create() };
	    for ( int t = 0 ; t < 3 ; t ++ ) { 
		    data[t].addColumn(ColumnType.STRING, "Title");
		    data[t].addColumn(ColumnType.NUMBER, "Allocated");    	
		    data[t].addRows(mList.size()-1);
		    for ( int i = 0 ; i < mList.size()-1 ; i ++ ) {
			    data[t].setValue(i, 0, mList.get(i+1).getTitle());
		    }
	    }
	    Boolean net = !mNetButton.isDown();
	    for ( int i = 0 ; i < mList.size()-1 ; i ++ ) {
	    	if ( ( mList.get(i+1).getOriginal( BudgetLine.ALLOCATED, net ) != null ) &&
	    		 ( mList.get(i+1).getOriginal( BudgetLine.ALLOCATED, net ) > 0 ) ) {
	    		data[0].setValue(i, 1, mList.get(i+1).getOriginal( BudgetLine.ALLOCATED, net ));
	    	} else {
	    		data[0].setValue(i, 1, 0 );	    		
	    	}
	    	if ( (mList.get(i+1).getOriginal( BudgetLine.REVISED, net ) != null) && 
	    		 (mList.get(i+1).getOriginal( BudgetLine.REVISED, net ) > 0) ) {
			    data[1].setValue(i, 1, mList.get(i+1).getOriginal( BudgetLine.REVISED, net ) );    		
	    	} else {
			    data[1].setValue(i, 1, 0);    			    		
	    	}
	    	if ( (mList.get(i+1).getOriginal( BudgetLine.USED, net ) != null) &&
	    		 (mList.get(i+1).getOriginal( BudgetLine.USED, net ) > 0) ) {
	    		data[2].setValue(i, 1, mList.get(i+1).getOriginal( BudgetLine.USED, net ) );
	    	} else {
	    		data[2].setValue(i, 1, 0);	    		
	    	}
	    }

	    PieChart piechartAllocated = new PieChart( data[0], options );
	    PieChart piechartRevised = new PieChart( data[1], options );
	    PieChart piechartUsed = new PieChart( data[2], options );

		mTabPanel.setWidth("325px");   
	    mTabPanel.add(piechartAllocated,"הקצאה");
		mTabPanel.add(piechartRevised,"הקצאה מעודכנת");
		mTabPanel.add(piechartUsed,"שימוש");
		mTabPanel.selectTab(1);
		mAllocatedButton.setDown(false);
		mRevisedButton.setDown(true);
		mUsedButton.setDown(false);
	}
}
