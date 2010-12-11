package org.obudget.client;

import com.google.gwt.event.logical.shared.ValueChangeEvent;
import com.google.gwt.event.logical.shared.ValueChangeHandler;
import com.google.gwt.json.client.JSONArray;
import com.google.gwt.user.client.History;

class Application implements ValueChangeHandler<String> {

	private BudgetLines mChildrenBudgetLines = new BudgetLines();
	private BudgetLines  mHistoricBudgetLines = new BudgetLines();
	private ResultGrid mResultsGrid;
	private PieCharter mPieCharter;
	private TimeLineCharter mTimeLineCharter;
	private String mCode = null;
	private Integer mYear = null;
	
	public void init() {
		mResultsGrid = new ResultGrid();
		mResultsGrid.setWidth("300px");

		mPieCharter = new PieCharter(this);
		mPieCharter.setWidth("600px");
		mPieCharter.setHeight("300px");
		
		mTimeLineCharter = new TimeLineCharter(this);
		mTimeLineCharter.setWidth("600px");
		mTimeLineCharter.setHeight("300px");
		
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

}
