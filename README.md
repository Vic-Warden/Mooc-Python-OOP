# Python OOP — Course Exercises

A structured collection of Python Object-Oriented Programming exercises, organized by concept.

## Structure

```
.
├── Bases_OOP/          # OOP fundamentals
├── Heritage/           # Inheritance patterns
├── Exceptions/         # Custom exceptions
├── Library/            # Mini-project: movie library
└── Projet/             # Mini-project: forum system
```

## Modules

### `Bases_OOP/`
| File | Concepts |
|------|----------|
| `rectangle.py` | Class declaration, attributes, constructor, methods |
| `car.py` | Single inheritance, `super()` |
| `toolbox.py` | Multiple classes, `__str__`, `__repr__`, object composition |

### `Heritage/`
| File | Concepts |
|------|----------|
| `abstract_classes.py` | Abstract base class (`ABC`), `@abstractmethod` |
| `overriding.py` | Method overriding, `super()` |
| `multiple_inheritance.py` | Multiple inheritance, MRO |
| `multi_level.py` | Multi-level inheritance chain |

### `Exceptions/`
| File | Concepts |
|------|----------|
| `exceptions.py` | Custom exception hierarchy |
| `user_models.py` | Raising and handling custom exceptions |
| `test.py` | Exception catching with `try/except` |

### `Library/`
A movie library app covering:
- Inheritance (`VHF`, `DVD` extend `Movie`)
- Object relationships (`Library`, `Friend`, `Movie`)
- Sorting and random selection

### `Projet/`
A basic forum system covering:
- Multi-level inheritance (`Post` → `FilePost`, `User` → `Moderator`)
- Object composition (`Thread` contains `Post` list, `Post` can hold a `File`)
- `__str__` override, role-based behavior (`Moderator.delete`)

## Requirements

- Python 3.8+
- No external dependencies

## Usage

Each file is standalone and can be run directly:

```bash
python Bases_OOP/toolbox.py
python Heritage/abstract_classes.py
python Library/app.py
python Projet/main.py
```