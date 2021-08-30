There are so many libraries out there for writing command line utilities; why does Click exist?

This question is easy to answer: because there is not a single command line utility for Python out there which ticks the following boxes:

Is lazily composable without restrictions.

Supports implementation of Unix/POSIX command line conventions.

Supports loading values from environment variables out of the box.

Support for prompting of custom values.

Is fully nestable and composable.

Supports file handling out of the box.

Comes with useful common helpers (getting terminal dimensions, ANSI colors, fetching direct keyboard input, screen clearing, finding config paths, launching apps and editors, etc.).
