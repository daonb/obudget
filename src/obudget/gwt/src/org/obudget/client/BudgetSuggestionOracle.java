package org.obudget.client;

import java.util.LinkedList;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.user.client.Timer;
import com.google.gwt.user.client.ui.SuggestOracle;

class BudgetSuggestionOracle extends SuggestOracle {

	private Boolean mAllowed = true;
	private Boolean mOngoing = false;
	private String mRequestQuery = null;
	private Timer mTimer; 

	private Callback mCallback;
	private Request mRequest;
	private String mRequestedQuery;

	public BudgetSuggestionOracle() {
		mTimer = new Timer() {
			@Override
			public void run() {
				mAllowed = true;
				doQuery();				
			}
		};
	}
	
	@Override
	public boolean isDisplayStringHTML() {
		return true;
	}

	private void doQuery() {
		if ( mRequestQuery != null &&
			 mAllowed &&
			 !mOngoing ) {
			
			mOngoing = true;
			mRequestedQuery = mRequestQuery;
			mRequestQuery = null;

			BudgetAPICaller api = new BudgetAPICaller();
			api.setParameter("text", mRequestedQuery);
			api.setParameter("full", "1");
			api.setParameter("num", "20");
			api.setParameter("distinct", "1");
			
			api.go(new BudgetAPICallback() {	
				@Override
				public void onSuccess(JSONArray array) {
					mOngoing = false;
					Response response = new Response();
					LinkedList<Suggestion> suggestions = new LinkedList<Suggestion>();
					for ( int i = 0 ; i < array.size() ; i ++ ) {
						String title = array.get(i).isObject().get("title").isString().stringValue();
						String code =  array.get(i).isObject().get("budget_id").isString().stringValue();
						JSONArray parentsArray = array.get(i).isObject().get("parent").isArray();
						String[] parents = new String[parentsArray.size()];
						for ( int j = 0 ; j < parentsArray.size() ; j++ ) {
							parents[j] = parentsArray.get(j).isObject().get("title").isString().stringValue();
						}
						Suggestion suggestion = new BudgetSuggestion(mRequestedQuery, title, code, parents);
						suggestions.add(suggestion);
					}
					response.setSuggestions( suggestions );
					mCallback.onSuggestionsReady(mRequest, response);
				}
			});	
			
		} else {
			if ( mAllowed ) {
				mAllowed = false;
				mTimer.schedule(500);
			}
		}
	}
	
	@Override
	public void requestSuggestions(final Request request, final Callback callback) {
		mCallback = callback;
		mRequest = request;
		mRequestQuery = request.getQuery();
		doQuery();
	}
	
}
