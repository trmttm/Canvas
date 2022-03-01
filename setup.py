from setuptools import setup

setup(
    name='Canvas',
    version='',
    packages=['apps', 'Tests', 'entities', 'entities.shapes', 'use_cases', 'use_cases.AddLine', 'use_cases.AddText',
              'use_cases.MoveLine', 'use_cases.MoveText', 'use_cases.RemoveLine', 'use_cases.RemoveText',
              'use_cases.SelectShape', 'use_cases.AddRectangle', 'use_cases.SetFillColor', 'use_cases.SetLineArrow',
              'use_cases.SetLineColor', 'use_cases.SetLineWidth', 'use_cases.SetTextColor', 'use_cases.SetTextValue',
              'use_cases.MoveRectangle', 'use_cases.SetBorderColor', 'use_cases.SetBorderWidth',
              'use_cases.RemoveRectangle', 'use_cases.SetTextFontSize', 'use_cases.SelectShapesInRange',
              'use_cases.ChangeRectangleShape', 'interactor', 'other_use_cases', 'complex_commands',
              'use_cases_high_level', 'use_cases_high_level.AddTextBox', 'use_cases_high_level.MoveTextBox',
              'use_cases_high_level.RemoveTextBox', 'use_cases_high_level.HighlightTextBox'],
    url='',
    license='',
    author='STTM',
    author_email='',
    description=''
)
