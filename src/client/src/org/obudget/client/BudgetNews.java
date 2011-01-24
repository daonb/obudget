package org.obudget.client;

import com.google.gwt.core.client.JsArray;
import com.google.gwt.dom.client.Element;
import com.google.gwt.search.client.LinkTarget;
import com.google.gwt.search.client.NewsResult;
import com.google.gwt.search.client.NewsSearch;
import com.google.gwt.search.client.Result;
import com.google.gwt.search.client.ResultClass;
import com.google.gwt.search.client.ResultSetSize;
import com.google.gwt.search.client.Search;
import com.google.gwt.search.client.SearchControl;
import com.google.gwt.search.client.SearchControlOptions;
import com.google.gwt.search.client.SearchResultsHandler;
import com.google.gwt.search.client.WebResult;
import com.google.gwt.search.client.SearchResultsHandler.SearchResultsEvent;
import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.user.client.ui.Grid;
import com.google.gwt.user.client.ui.LayoutPanel;
import com.google.gwt.user.client.ui.VerticalPanel;

public class BudgetNews extends Composite {
	
	private SearchControl mControl;
	private Grid mGrid;
	private LayoutPanel mPanel;

	private native void attachBranding(Element element)/*-{
	if ($wnd.google.load) {
		$wnd.google.load("search", "1", {"callback" : function() {
			$wnd.google.search.Search.getBranding(element);
		}});
	}
}-*/;
	
	public BudgetNews() {

	    mGrid = new Grid(10, 1);
	    mGrid.setWidth("220px");

	    NewsSearch newsSearch = new NewsSearch();
	    newsSearch.setResultSetSize(ResultSetSize.SMALL);
	    newsSearch.setQueryAddition("+תקציב");
	    newsSearch.setNoHtmlGeneration();

	    SearchControlOptions options = new SearchControlOptions();
	    options.add(newsSearch);
	    options.setLinkTarget(LinkTarget.BLANK);
	        
	    mControl = new SearchControl(options);
	    mControl.addSearchResultsHandler(new SearchResultsHandler() {
			
			@Override
			public void onSearchResults(SearchResultsEvent event) {
				JsArray<? extends Result> results = event.getResults();
				mGrid.resizeRows(0);
				if ( results.length() == 0 ) { return; }
				mGrid.resizeRows(results.length());
				int currentRow = 0;
				for ( int i = 0 ; i < results.length() && currentRow < 10 ; i ++ ) {
				     if (results.get(i).getResultClass().equals(ResultClass.NEWS_SEARCH_RESULT)) {
			            NewsResult result = (NewsResult) results.get(i);
			            String html = result.getPublisher()+":&nbsp;<a href='"+result.getUnescapedUrl()+"' target='_blank'>"+result.getTitleNoFormatting()+"</a>";	            				            	
			            mGrid.setHTML(currentRow, 0, html);
			            currentRow++;
				     }					
				}
				attachBranding(mPanel.getElement());
				//mGrid.setHTML(currentRow, 0, );
			}
		});
	    
	    VerticalPanel vPanel = new VerticalPanel();
	    mPanel = new LayoutPanel();
	    vPanel.add(mGrid);
	    vPanel.add(mPanel);
	    initWidget(vPanel);
	}
	
	public void update( String query ) {
	    mControl.execute(query);
	}
}
