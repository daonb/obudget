package org.obudget.client;

import com.google.gwt.core.client.GWT;
import com.google.gwt.user.client.ui.SuggestOracle.Suggestion;

class BudgetSuggestion implements Suggestion {

	private String mCode;
	private String mQuery;
	private String mTitle;
	private String[] mParents;

	public BudgetSuggestion(String query, String title, String code, String[] parents) {
		mTitle = title;
		mCode = code;
		mQuery = query;
		mParents = parents;
	}
	
	@Override
	public String getDisplayString() {
		String suggestion = mCode + " - "  + mTitle;
		suggestion = suggestion.replace(mQuery, "<b>"+mQuery+"</b>");
		
		String parents = "";
		for ( int i = mParents.length-2 ; i >= 0 ; i-- ) {
			parents += mParents[i];
			if ( i != 0 ) {
				parents += " &gt; ";
			}
		}
		
		if ( !parents.equals("") ) {
			suggestion = suggestion + "&nbsp;&nbsp;<span style='font-size:60%'>("+parents+")</span>";
		}
		return suggestion;
	}

	@Override
	public String getReplacementString() {
		return mTitle;
	}
		
	public String getCode() {
		return mCode;
	}

	public String getTitle() {
		return mTitle;
	}
	
}

