package org.obudget.client;

import com.google.gwt.json.client.JSONArray;

interface BudgetAPICallback {
	void onSuccess( JSONArray data );
}