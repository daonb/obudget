package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.user.client.ui.Grid;
import com.google.gwt.user.client.ui.Label;

class HeaderLabel extends Label {
	public HeaderLabel(String contents) {
		super(contents);
		setWordWrap(false);
		setStylePrimaryName("resultgrid-header");
	}
}

class ResultGrid extends Composite {
	private Grid mGrid;

	public ResultGrid( ) {
		mGrid = new Grid(1,4);
		mGrid.setStylePrimaryName("resultgrid");
		mGrid.setCellSpacing(0);
		initWidget(mGrid);
	}
	
	public void handleData( LinkedList<BudgetLine> list ) {
		mGrid.resizeRows(list.size()+1);

		HeaderLabel name = new HeaderLabel("שם");
		HeaderLabel allocated = new HeaderLabel("הקצאה");
		HeaderLabel revised = new HeaderLabel("הקצאה מעודכנת");
		HeaderLabel used = new HeaderLabel("שימוש");
		
		mGrid.setWidget(0, 0, name );
		mGrid.setWidget(0, 1, allocated );
		mGrid.setWidget(0, 2, revised );
		mGrid.setWidget(0, 3, used );

		for ( int r = 0 ; r < list.size() ; r ++ ) {
			BudgetLine bl = list.get(r);
			mGrid.setHTML(r+1, 0, "<a href='#"+bl.getCode()+","+bl.getYear()+"'>"+bl.getTitle()+"</a>" );
			mGrid.setText(r+1, 1, "" + bl.getAllocated() );
			mGrid.setText(r+1, 2, "" + bl.getRevised() );
			mGrid.setText(r+1, 3, "" + bl.getUsed() );			
			mGrid.getCellFormatter().addStyleName(r+1, 1, "resultgrid-data");
			mGrid.getCellFormatter().addStyleName(r+1, 2, "resultgrid-data");
			mGrid.getCellFormatter().addStyleName(r+1, 3, "resultgrid-data");
		}

		mGrid.getRowFormatter().addStyleName(0, "resultgrid-header-row");
		mGrid.getRowFormatter().addStyleName(1, "resultgrid-totals-row");

	}
}
