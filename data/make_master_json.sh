#!/bin/bash
cat financial_report/2000-2008/out.json \
    financial_report/2009/out.json \
    history_neto/history.json \
    2010_planned/out.json \
    2011_planned/out.json \
                                > master.json
