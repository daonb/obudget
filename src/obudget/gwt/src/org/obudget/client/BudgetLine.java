package org.obudget.client;

class BudgetLine {
	private Integer mUsed;
	private Integer mRevised;
	private Integer mAllocated;
	private String mTitle;
	private String mCode;
	private Integer mYear;
	private Double mInflation;

	public BudgetLine( String title, 
					   Integer allocated,
					   Integer revised,
					   Integer used,
					   String code,
					   Integer year,
					   Double inflation) {
		mTitle = title;
		mAllocated = allocated;
		mRevised = revised;
		mUsed = used;
		mCode = code;
		mYear = year;
		mInflation = inflation;
	}

	public Integer getAllocated() {
		return mAllocated;
	}

	public Integer getInfAllocated() {
		return (int) (mInflation * mAllocated);
	}

	public Double getPercentAllocated() {
		return 100.0 * mAllocated / TotalBudget.getInstance().getAllocated(mYear);
	}

	public Integer getRevised() {
		return mRevised;
	}

	public Integer getInfRevised() {
		return (int) (mInflation * mRevised);
	}

	public Double getPercentRevised() {
		return 100.0 * mRevised / TotalBudget.getInstance().getRevised(mYear);
	}

	public Integer getUsed() {
		return mUsed;
	}

	public Integer getInfUsed() {
		return (int) (mInflation * mUsed);
	}

	public Double getPercentUsed() {
		return 100.0 * mUsed / TotalBudget.getInstance().getUsed(mYear);
	}

	public String getTitle() {
		return mTitle;
	}

	public String getCode() {
		return mCode;
	}

	public Integer getYear() {
		return mYear;
	}
}
