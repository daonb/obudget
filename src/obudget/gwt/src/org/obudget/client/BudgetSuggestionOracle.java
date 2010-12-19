package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.SuggestOracle;

class BudgetSuggestionOracle extends SuggestOracle {

	private ListBox mYearSelection;

	public BudgetSuggestionOracle(ListBox yearSelection) {
		mYearSelection = yearSelection;
	}
	
	@Override
	public boolean isDisplayStringHTML() {
		return true;
	}

	@Override
	public void requestSuggestions(final Request request, final Callback callback) {
		final String query = request.getQuery();
		
		BudgetAPICaller api = new BudgetAPICaller();
		api.setParameter("text", query);
		api.setParameter("full", "1");
		api.setParameter("num", "20");
		api.setParameter("distinct", "1");
		api.go(new BudgetAPICallback() {
			
			@Override
			public void onSuccess(JSONArray array) {
				Response response = new Response();
				LinkedList<Suggestion> suggestions = new LinkedList<Suggestion>();
				for ( int i = 0 ; i < array.size() ; i ++ ) {
					String title = array.get(i).isObject().get("title").isString().stringValue();
					String code =  array.get(i).isObject().get("budget_id").isString().stringValue();
					Suggestion suggestion = new BudgetSuggestion(query, title, code);
					suggestions.add(suggestion);
				}
				response.setSuggestions( suggestions );
				callback.onSuggestionsReady(request, response);
			}
			
		});
	}
	
}
