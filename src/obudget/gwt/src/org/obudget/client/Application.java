package org.obudget.client;

import com.google.gwt.event.dom.client.ChangeEvent;
import com.google.gwt.event.dom.client.ChangeHandler;
import com.google.gwt.event.logical.shared.SelectionEvent;
import com.google.gwt.event.logical.shared.SelectionHandler;
import com.google.gwt.event.logical.shared.ValueChangeEvent;
import com.google.gwt.event.logical.shared.ValueChangeHandler;
import com.google.gwt.json.client.JSONArray;
import com.google.gwt.user.client.History;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.SuggestBox;
import com.google.gwt.user.client.ui.Widget;
import com.google.gwt.user.client.ui.SuggestOracle.Suggestion;

class Application implements ValueChangeHandler<String> {

	private BudgetLines mChildrenBudgetLines = new BudgetLines();
	private BudgetLines  mHistoricBudgetLines = new BudgetLines();
	private ResultGrid mResultsGrid;
	private PieCharter mPieCharter;
	private TimeLineCharter mTimeLineCharter;
	private String mCode = null;
	private Integer mYear = null;
	private ListBox mYearSelection;
	private SuggestBox mSearchBox;
	
	public void init() {
		mResultsGrid = new ResultGrid();
		mResultsGrid.setWidth("300px");

		mPieCharter = new PieCharter(this);
		mPieCharter.setWidth("600px");
		mPieCharter.setHeight("300px");
		
		mTimeLineCharter = new TimeLineCharter(this);
		mTimeLineCharter.setWidth("600px");
		mTimeLineCharter.setHeight("300px");
		
		mYearSelection = new ListBox();
		mYearSelection.addChangeHandler( new ChangeHandler() {
			@Override
			public void onChange(ChangeEvent event) {
				Integer index = mYearSelection.getSelectedIndex();
				if ( index > 0 ) {
					selectYear( 1991+index );
				}				
			}
		});
		
		mSearchBox = new SuggestBox(new BudgetSuggestionOracle(mYearSelection));
		mSearchBox.setWidth("300px");
		mSearchBox.addSelectionHandler( new SelectionHandler<Suggestion>() {
			@Override
			public void onSelection(SelectionEvent<Suggestion> event) {
				BudgetSuggestion bs = (BudgetSuggestion) event.getSelectedItem();
				History.newItem(bs.getCode() +","+ bs.getYear() );
			}
		});

		mYearSelection.addItem("כולן");
		for ( Integer i = 1992 ; i<=2009 ; i ++ ) {
			mYearSelection.addItem(i.toString());
		}

		History.addValueChangeHandler( this );
	}

	public ResultGrid getResultsGrid() {
		return mResultsGrid;
	}

	public PieCharter getPieCharter() {
		return mPieCharter;
	}

	public void selectYear( Integer year ) {
		if ( mCode != null ) {
			selectBudgetCode(mCode, year);
		}
	}

	public void selectBudgetCode( String code, Integer year ) {
		mCode = code;
		mYear = year;
		
		BudgetAPICaller generalInfo = new BudgetAPICaller();
		generalInfo.setCode(code);
		generalInfo.setParameter("year", year.toString() );
		generalInfo.setParameter("depth", "0");
		generalInfo.go( new BudgetAPICallback() {
			
			@Override
			public void onSuccess(JSONArray data) {
				if ( data.size() < 1 ) {
					return;
				}
				String title = data.get(0).isObject().get("title").isString().stringValue();
				String code = data.get(0).isObject().get("budget_id").isString().stringValue();
				
				Window.setTitle("תקציב המדינה - "+title+" ("+mYear+")");
				mYearSelection.setSelectedIndex( mYear - 1991 );
				mSearchBox.setValue(code + " - " + title + " ("+mYear+")" );				
			}
		});

		BudgetAPICaller childrenLines = new BudgetAPICaller();
		childrenLines.setCode(code);
		childrenLines.setParameter("year", year.toString());
		childrenLines.setParameter("depth", "1");
		childrenLines.go( new BudgetAPICallback() {
			
			@Override
			public void onSuccess(JSONArray data) {
				mChildrenBudgetLines.parseJson(data);
				mResultsGrid.handleData(mChildrenBudgetLines);
				mPieCharter.handleData(mChildrenBudgetLines);				
			}
		});
		
		BudgetAPICaller historicLines = new BudgetAPICaller();
		historicLines.setCode(code);
		historicLines.setParameter("depth", "0");
		historicLines.go( new BudgetAPICallback() {
			
			@Override
			public void onSuccess(JSONArray data) {
				mHistoricBudgetLines.parseJson(data);
				mTimeLineCharter.handleData(mHistoricBudgetLines);				
			}
		});
		
	}

	public TimeLineCharter getTimeLineCharter() {
		return mTimeLineCharter;
	}

	@Override
	public void onValueChange(ValueChangeEvent<String> event) {
		String hash = event.getValue();
		String[] parts = hash.split(",");
		if ( parts.length == 2 ) {
			String code = parts[0];
			Integer year = Integer.decode(parts[1]);
			selectBudgetCode(code, year);
		}
	}

	public Widget getYearSelection() {
		return mYearSelection;
	}

	public Widget getSearchBox() {
		return mSearchBox;
	}

}
