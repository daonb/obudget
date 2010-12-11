package org.obudget.client;

import com.google.gwt.user.client.ui.SuggestOracle.Suggestion;

class BudgetSuggestion implements Suggestion {

	private String mSuggestion;
	private String mCode;
	private Integer mYear;

	public BudgetSuggestion(String title, String code, Integer year) {
		mSuggestion = code + " - "  + title + " (" + year + ")";
		mCode = code;
		mYear = year;
	}
	
	@Override
	public String getDisplayString() {
		return mSuggestion;
	}

	@Override
	public String getReplacementString() {
		return mSuggestion;
	}
	
	public Integer getYear() {
		return mYear;
	}
	
	public String getCode() {
		return mCode;
	}
	
}

