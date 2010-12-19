package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.i18n.client.NumberFormat;
import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.user.client.ui.Grid;
import com.google.gwt.user.client.ui.HTML;
import com.google.gwt.user.client.ui.Label;

class ResultGrid extends Composite {
	private Grid mGrid;

	class HeaderLabel extends Label {
		public HeaderLabel(String contents) {
			super(contents);
			setWordWrap(false);
			setStylePrimaryName("resultgrid-header");
		}
	}

	public ResultGrid() {
		mGrid = new Grid(1,4);
		mGrid.setStylePrimaryName("resultgrid");
		mGrid.setCellSpacing(0);
		mGrid.setCellPadding(2);
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
			String title;
			if ( r != 0 ) {
				title = "&nbsp;&nbsp;" + "<a href='#"+bl.getCode()+","+bl.getYear()+"'>"+bl.getTitle()+"</a>";
			} else {
				title = "סה\"כ:";				
			}
			HTML titleHtml = new HTML(title);
			titleHtml.setWordWrap(false);
			mGrid.setWidget(r+1, 0, titleHtml);
			NumberFormat decimalFormat = NumberFormat.getDecimalFormat();
			mGrid.setText(r+1, 1, decimalFormat.format( bl.getAllocated() )+ (bl.getAllocated() == 0 ? "" : ",000") );
			mGrid.setText(r+1, 2, decimalFormat.format( bl.getRevised() )+ (bl.getRevised() == 0 ? "" : ",000") );
			mGrid.setText(r+1, 3, decimalFormat.format( bl.getUsed() )+ (bl.getUsed() == 0 ? "" : ",000") );			
			mGrid.getCellFormatter().addStyleName(r+1, 1, "resultgrid-data");
			mGrid.getCellFormatter().addStyleName(r+1, 2, "resultgrid-data");
			mGrid.getCellFormatter().addStyleName(r+1, 3, "resultgrid-data");
		}

		mGrid.getRowFormatter().addStyleName(0, "resultgrid-header-row");
		if ( mGrid.getRowCount() > 1 ) { 
			mGrid.getRowFormatter().addStyleName(1, "resultgrid-totals-row");
		}

	}
}
