#!/usr/bin/env python3

"""

	Ah fuck, quick-and-dirty solution time.

	Rationale:
		Split the contest into two cases, completing an "engulfed" expression and completing an "external" extression.
		Ex: Engulfed: "[2+3+4)]", the paren-completion is surrounded by completed bracks.
		Ex: External: "[2+(3+4)", the brack-completion contains a completed parens.
	We can detect this by detecting completed bracks/parens, and checking if that string splice contains a brack/paren.

"""
