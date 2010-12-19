package org.obudget.client;

import com.google.gwt.core.client.GWT;
import com.google.gwt.user.client.ui.SuggestOracle.Suggestion;

class BudgetSuggestion implements Suggestion {

	private String mSuggestion;
	private String mCode;
	private String mQuery;
	private String mTitle;

	public BudgetSuggestion(String query, String title, String code) {
		mSuggestion = code + " - "  + title;
		mTitle = title;
		mCode = code;
		mQuery = query;
	}
	
	@Override
	public String getDisplayString() {
		return mSuggestion.replace(mQuery, "<b>"+mQuery+"</b>");
	}

	@Override
	public String getReplacementString() {
		return mSuggestion;
	}
		
	public String getCode() {
		return mCode;
	}

	public String getTitle() {
		return mTitle;
	}
	
}

