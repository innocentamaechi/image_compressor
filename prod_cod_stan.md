---

# Production Code Standards

Every line of code committed to this project should be considered production-ready. The goal is to build software that is maintainable, secure, testable, and deployable from the start, rather than relying on future rewrites.

## Guiding Principle

> Write code that is good enough to deploy, not just good enough to demonstrate.

This does **not** mean over-engineering the project. It means writing clean, reliable, and maintainable code while keeping the MVP as small as possible.

---

## Production Requirements

Every file must:

- Have a single, well-defined responsibility.
- Include module, class, and function docstrings where appropriate.
- Use Python type hints.
- Handle expected errors gracefully.
- Avoid hardcoded values where configuration is more appropriate.
- Follow PEP 8 coding standards.
- Use meaningful and descriptive names.
- Be modular and easy to test.
- Include logging where it adds value.
- Avoid duplicated code.
- Validate external input.
- Fail safely with clear error messages.
- Be written with readability and maintainability as the primary goals.

---

## What We Will Not Write

This project intentionally avoids:

- Tutorial-style code.
- Quick hacks or temporary fixes.
- Placeholder implementations that are expected to be rewritten later.
- Unnecessary abstractions.
- Over-engineered solutions.
- Copy-pasted code without understanding it.
- Functions or classes with multiple unrelated responsibilities.
- Dead code or unused files.

---

## Development Workflow

Every feature should follow this process:

1. Define the requirement.
2. Design the implementation.
3. Review any new dependencies.
4. Write production-quality code.
5. Explain architectural decisions when necessary.
6. Verify the implementation before moving to the next feature.

No feature is considered complete until it satisfies the project's quality standards.

---

## File Size Guidelines

Files should remain focused and easy to understand.

As a general guideline:

- Aim to keep files between **100 and 300 lines** whenever practical.
- If a file grows beyond **500 lines** or begins handling multiple responsibilities, it should be reviewed for refactoring.
- Split functionality into smaller modules only when it improves clarity and maintainability—not simply to reduce line count.

---

## Simplicity First

Production-ready does **not** mean enterprise complexity.

The project should always favor:

- Simplicity over cleverness.
- Clarity over brevity.
- Readability over unnecessary optimization.
- Maintainability over premature abstraction.

The MVP should remain as small as possible while still meeting production-quality standards.

---

## Code Review Checklist

Before considering any code complete, verify the following:

- [ ] The code solves the intended problem.
- [ ] The solution is as simple as reasonably possible.
- [ ] No unnecessary dependencies were introduced.
- [ ] The code follows the project's architecture.
- [ ] Public functions include type hints and documentation.
- [ ] Error handling is appropriate.
- [ ] Inputs are validated.
- [ ] Logging is included where useful.
- [ ] Naming is clear and consistent.
- [ ] No duplicated logic exists.
- [ ] The code is maintainable by another developer without additional explanation.

---

## Long-Term Goal

The objective is to build a codebase that:

- Is easy to understand.
- Is easy to extend.
- Is easy to test.
- Is easy to hand over to another developer or AI assistant.
- Can evolve over time without requiring major rewrites.

Every commit should move the project toward that goal.
