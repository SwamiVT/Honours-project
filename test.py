#!/usr/bin/env python3
"""Simple PsychoPy sanity check.

What it does:
1) Verifies PsychoPy can be imported.
2) Opens a window.
3) Shows text, then a basic visual stimulus.
4) Waits for a key press (or times out) and exits cleanly.
"""

from __future__ import annotations

import sys
from typing import NoReturn


def fail_with_install_message() -> NoReturn:
	print("PsychoPy is not installed or could not be imported.")
	print("Install it with one of these commands:")
	print("  pip install psychopy")
	print("  python -m pip install psychopy")
	raise SystemExit(1)


def main() -> int:
	try:
		from psychopy import core, event, visual
	except Exception:
		fail_with_install_message()

	win = None
	try:
		win = visual.Window(size=(900, 600), color="black", units="height", fullscr=False)

		intro = visual.TextStim(
			win,
			text="PsychoPy import successful!\nShowing simple text and stimulus...",
			color="white",
			height=0.06,
			wrapWidth=1.4,
		)

		circle = visual.Circle(
			win,
			radius=0.12,
			fillColor="red",
			lineColor="white",
			pos=(0, 0.05),
		)

		prompt = visual.TextStim(
			win,
			text="If you can see this red circle, PsychoPy visuals are working.\n"
			"Press any key to quit (auto-exit in 8 seconds).",
			color="white",
			height=0.04,
			pos=(0, -0.28),
			wrapWidth=1.6,
		)

		# Screen 1: intro text
		intro.draw()
		win.flip()
		core.wait(2.0)

		# Screen 2: simple visual stimulus + text
		circle.draw()
		prompt.draw()
		win.flip()

		keys = event.waitKeys(maxWait=8.0)
		if not keys:
			print("No key pressed within 8 seconds. Closing automatically.")

		print("PsychoPy test completed successfully.")
		return 0

	except Exception as exc:
		print(f"PsychoPy test failed: {exc}")
		return 2
	finally:
		try:
			if win is not None:
				win.close()
		finally:
			try:
				# Import here as a fallback in case the earlier import block failed unexpectedly.
				from psychopy import core

				core.quit()
			except Exception:
				pass


if __name__ == "__main__":
	sys.exit(main())
