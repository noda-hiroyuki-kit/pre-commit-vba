# Accessibility

[**日本語はこちら**](ACCESSIBILITY_JA.md)

We want people with disabilities and people using assistive technology to be
able to use and contribute to `pre-commit-vba`.

This statement covers the command-line interface, repository documentation,
and [documentation website](https://noda-hiroyuki-kit.github.io/pre-commit-vba/).
It describes our goals, contributor guidance, and how to report barriers.

## Accessibility Goals

We aim to make the project easier to use by:

- Providing understandable command help, error messages, and next steps.
- Keeping important command output available as text, without relying only on
  color or visual formatting.
- Writing clear documentation with descriptive links, meaningful headings,
  and text alternatives for images and demonstrations.
- Making documentation navigation usable with a keyboard and assistive
  technology.
- Keeping English and Japanese documentation aligned when making changes.

For the documentation website, we use
[WCAG 2.2 Level AA](https://www.w3.org/TR/WCAG22/) as an improvement target,
not a claim of verified conformance.

## Guidance for Contributors

Please consider accessibility when changing user-facing behavior or content:

- Use a logical heading structure and descriptive link text.
- Provide useful alternative text for images and a nearby text explanation
  for diagrams or demonstrations.
- Include captions and a transcript when adding video content.
- Do not communicate errors, status, or instructions through color alone.
- Keep CLI messages understandable when read as plain text or aloud.
- For website navigation or interactive changes, check keyboard operation,
  visible focus, and whether users can move into and out of controls.
- Check affected pages at increased zoom and narrow widths for lost content
  or functionality.
- Where possible, check significant user-facing changes with a screen reader.

In your pull request, describe the accessibility checks you performed, their
results, and any limitations you could not verify. Automated checks can help,
but do not replace checking how people use the affected feature.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the general contribution process.

## Reporting an Accessibility Barrier

Please [open an issue](https://github.com/noda-hiroyuki-kit/pre-commit-vba/issues/new)
and identify it as an accessibility report. You can also use this channel to
request a more accessible explanation of documentation or command output.

Include whatever information you can provide:

- The task you were trying to complete and the barrier you encountered.
- The affected command, output, or page URL.
- Steps that help reproduce the problem and the result you expected.
- The project version, operating system, terminal or browser, and assistive
  technology, if relevant.
- A possible workaround or suggested improvement.

Screenshots and recordings are optional. You do not need to disclose a
disability, diagnosis, or other personal information. GitHub issues are public;
remove credentials, confidential Office documents, and other sensitive data
from any examples or attachments.

Report suspected security vulnerabilities privately as described in
[SECURITY.md](SECURITY.md), rather than in an accessibility issue.

## How Reports Are Handled

Project maintainers review accessibility reports and prioritize barriers based
on their impact, especially those that prevent people from completing a task.
We may ask for clarification, share a workaround, or invite you to check a
proposed fix. Progress and known limitations can be tracked in the issue.

Response and resolution times depend on maintainer availability and the scope
of the work; we do not guarantee a fixed deadline.

## Scope and Limitations

This statement does not certify compatibility with specific screen readers,
terminals, browsers, or combinations of assistive technology.
Accessibility may also depend on Microsoft Office, the operating system,
terminal software, or third-party documentation components. Please report
barriers even when their source is unclear so we can investigate and identify
possible alternatives.

Maintainers are responsible for reviewing this statement as the project and
its accessibility practices change. Suggestions for improving the statement
are welcome through issues and pull requests.
