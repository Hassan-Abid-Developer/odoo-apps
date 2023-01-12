# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Pakistan Payroll',
    'version': '15.0.1.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Pakistan Payroll Localization',
    'depends': ['hr_payroll'],
    'author': 'Hassan Abid',
    'description': """
        Pakistan Payroll Salary Rules.
    ============================

    -Configuration of hr_payroll for Pakistan localization
    -All main contributions rules for Pakistan payslip.
    * New payslip report
    * Employee Contracts
    * Allow to configure Basic / Gross / Net Salary
    * Employee PaySlip.
    * Allowance / Deduction
    * Integrated with Leaves Management
    * Medical Allowance, Travel Allowance, Child Allowance, ...
    - Payroll Advice and Report
    - Yearly Salary by Head and Yearly Salary by Employee Report
    """,
    'data': [
        'views/l10n_pk_hr_payroll_view.xml',
        'views/hr_employee_view.xml',
        
        'data/l10n_pk_hr_payroll_data.xml',
        'data/l10n_pk_hr_payroll_rule_data.xml',
        
        'security/ir.model.access.csv',
        
        'views/l10n_pk_hr_payroll_report.xml',
       
        'data/l10n_pk_hr_payroll_sequence_data.xml',
        
        'views/report_payslip_details_template.xml',
        'views/report_hr_salary_employee_bymonth_template.xml',
        
        'wizard/hr_salary_employee_bymonth_view.xml',
        'wizard/hr_yearly_salary_detail_view.xml',
        
        'views/report_hr_yearly_salary_detail_template.xml',
        'views/report_payroll_advice_template.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'OEEL-1',
}
