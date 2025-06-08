# CHANGELOG


## v1.3.2 (2025-06-08)

### Bug Fixes

- Correct Renovate configuration for dependency-groups
  ([#57](https://github.com/K-dash/flake8-import-guard/pull/57),
  [`25080f7`](https://github.com/K-dash/flake8-import-guard/commit/25080f7b6d3ab01e58ba469ff95420f54fbffc4c))

Replace unsupported 'pep735' manager with 'dependency-groups' depType. PEP 735 dependency-groups are
  automatically handled by the pep621 manager.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-authored-by: Claude <noreply@anthropic.com>

### Chores

- Migrate from Dependabot to Renovate Bot
  ([#55](https://github.com/K-dash/flake8-import-guard/pull/55),
  [`4bcd52f`](https://github.com/K-dash/flake8-import-guard/commit/4bcd52fb7356142296297e7e7a82e8372f9bc37d))

- Replace .github/dependabot.yml with .github/renovate.json - Add support for PEP 735
  dependency-groups in pyproject.toml - Configure Renovate Bot with auto-merge for minor/patch
  updates - Enable dependency dashboard and lock file maintenance - Set Asia/Tokyo timezone and
  appropriate scheduling

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-authored-by: Claude <noreply@anthropic.com>

- Update dev dependency packages ([#54](https://github.com/K-dash/flake8-import-guard/pull/54),
  [`28d5291`](https://github.com/K-dash/flake8-import-guard/commit/28d5291c1e3c5a095872072d7a75ff58d011b527))


## v1.3.1 (2025-06-08)

### Continuous Integration

- Add pull request validation workflow
  ([#49](https://github.com/K-dash/flake8-import-guard/pull/49),
  [`767c79c`](https://github.com/K-dash/flake8-import-guard/commit/767c79c4623cf0c2782e7f5b168ab68c4da7b4fc))

* ci: add pull request validation workflow

- Add GitHub Actions workflow to verify PR titles follow conventional commits - Configure commitlint
  to validate commit messages - Include labeler action (currently disabled)

* ci: add commitlint config

* ci: fix commit lint config

* ci: fix pr.yml

- Pined action ([#50](https://github.com/K-dash/flake8-import-guard/pull/50),
  [`fe3e1e3`](https://github.com/K-dash/flake8-import-guard/commit/fe3e1e31e263beb2f4047332b1256eb9cc02c1d5))

### Performance Improvements

- Add codspeed benchmarks ([#53](https://github.com/K-dash/flake8-import-guard/pull/53),
  [`c679a96`](https://github.com/K-dash/flake8-import-guard/commit/c679a965635c8d635d4cd540bac42f7488f9797d))

* ci: pined action

* perf: add CodSpeed benchmarking infrastructure

- Add pytest-codspeed dependency for performance testing - Create benchmark tests for core
  functionality: - AST import extraction performance - Forbidden import checking with various
  configurations - Nested module handling - Complex import pattern processing - Add GitHub Actions
  workflow for automated benchmarking - Configure CodSpeed to run on main branch pushes and PRs

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>

---------

Co-authored-by: Claude <noreply@anthropic.com>

Co-authored-by: Copilot Autofix powered by AI
  <62310815+github-advanced-security[bot]@users.noreply.github.com>


## v1.3.0 (2025-05-17)

### Build System

- Derive wheel version dynamically ([#44](https://github.com/K-dash/flake8-import-guard/pull/44),
  [`c2f0f6c`](https://github.com/K-dash/flake8-import-guard/commit/c2f0f6c1712bcefc8d9da0f0cce7b2544e233084))

### Chores

- Change package ecosystem in dependabot.yml from “pip” to “uv” and set target branch to “main
  ([#40](https://github.com/K-dash/flake8-import-guard/pull/40),
  [`59bba3a`](https://github.com/K-dash/flake8-import-guard/commit/59bba3a7c566dfd44ce50eb5d6f47a9590f9d9a1))

- **deps**: Bump flake8 from 7.1.2 to 7.2.0
  ([#42](https://github.com/K-dash/flake8-import-guard/pull/42),
  [`ec99096`](https://github.com/K-dash/flake8-import-guard/commit/ec99096d5df10ecf1d5b059684c89f6dbf8c4b54))

Bumps [flake8](https://github.com/pycqa/flake8) from 7.1.2 to 7.2.0. -
  [Commits](https://github.com/pycqa/flake8/compare/7.1.2...7.2.0)

--- updated-dependencies: - dependency-name: flake8 dependency-type: direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

### Documentation

- Fix formatting in contributing guide
  ([#45](https://github.com/K-dash/flake8-import-guard/pull/45),
  [`a72b4a6`](https://github.com/K-dash/flake8-import-guard/commit/a72b4a64595fc4a1ece65de151ce2ccf76b86775))

### Features

- Add type hints support and modernize type annotations
  ([#48](https://github.com/K-dash/flake8-import-guard/pull/48),
  [`905d1ac`](https://github.com/K-dash/flake8-import-guard/commit/905d1ac6feaa30c53e24bb2e7acb4a8425c7a8b6))

- Refactor type hints to use built-in collection types (PEP 585) - Move Generator import to
  collections.abc - Add py.typed marker file for better IDE support - Update build configuration to
  include type information

### Testing

- Verify __iter__ delegates to run ([#46](https://github.com/K-dash/flake8-import-guard/pull/46),
  [`a0b0521`](https://github.com/K-dash/flake8-import-guard/commit/a0b0521213a7f86e1fefc964c990d635691ae989))


## v1.2.0 (2025-03-29)

### Features

- Deprecated python3.8 ([#39](https://github.com/K-dash/flake8-import-guard/pull/39),
  [`b0c861b`](https://github.com/K-dash/flake8-import-guard/commit/b0c861b84337c47d893eb698ff80add80d506d2c))


## v1.1.0 (2025-03-29)

### Bug Fixes

- Semantic-release.yml
  ([`633aa35`](https://github.com/K-dash/flake8-import-guard/commit/633aa3584ad3283765393e71d9907b5bd40ea0e4))

- Update dev setup to use uv package manager
  ([`9ee9604`](https://github.com/K-dash/flake8-import-guard/commit/9ee9604110a2194f667dce8f50bc25dda962ab29))

Streamlines development setup process by adopting uv for dependency management Simplifies Makefile
  install target using `uv sync` Updates documentation with uv installation instructions

Enhances development experience with faster and more reliable package management

### Chores

- Consolidates CI workflows into Makefile
  ([`9b94b26`](https://github.com/K-dash/flake8-import-guard/commit/9b94b26902fb341a3774903ec6c10accfd9e1a91))

Removes separate GitHub Actions workflow files for linting and testing Moves CI test configuration
  into Makefile for better maintainability Introduces test-ci target that matches previous GitHub
  Actions setup

Simplifies CI configuration by centralizing build and test commands Maintains same coverage
  reporting functionality

- Updated dependencies: gitpython, ruff, pytest, pytest-cov versions
  ([`2623626`](https://github.com/K-dash/flake8-import-guard/commit/262362696343f5d74c34af822ffc309824cdb69c))

### Continuous Integration

- Implement semantic-release with English changelog sections
  ([`c60a0a9`](https://github.com/K-dash/flake8-import-guard/commit/c60a0a9d42496820b868795ba88154873ea4f303))

- Add python-semantic-release configuration - Create semantic-release GitHub workflow - Update
  contributing guide with conventional commits style - Add version variable to package __init__.py

- Update semantic-release command to use uv
  ([`67a9327`](https://github.com/K-dash/flake8-import-guard/commit/67a9327f2678ca3118745c2d88189baa2b669ca0))

### Features

- Deprecated python3.8
  ([`9f9cd90`](https://github.com/K-dash/flake8-import-guard/commit/9f9cd90af81fda8998b3457337e2eddd54adb2d3))

feat: deprecated python3.8

- Deprecated python3.8
  ([`cbeab59`](https://github.com/K-dash/flake8-import-guard/commit/cbeab59f1a225a6e85b92fbbaf3c63df8a2e9a28))

- Deprecated python3.8 ([#36](https://github.com/K-dash/flake8-import-guard/pull/36),
  [`7b9adc6`](https://github.com/K-dash/flake8-import-guard/commit/7b9adc69d022d6b779e2441cae26bf25630af419))

- Deprecated python3.8 ([#37](https://github.com/K-dash/flake8-import-guard/pull/37),
  [`24a47c4`](https://github.com/K-dash/flake8-import-guard/commit/24a47c455c06c1cc96162aa07d1858a4795bb097))

- Deprecated python3.8 ([#38](https://github.com/K-dash/flake8-import-guard/pull/38),
  [`a09c491`](https://github.com/K-dash/flake8-import-guard/commit/a09c4910ae0406590a998e122e8af7ec8820c407))

- Improve-ci
  ([`7d69da6`](https://github.com/K-dash/flake8-import-guard/commit/7d69da699b093231dd5623723eeefcc276de40fe))

- Migrate-poetry-to-uv
  ([`bfa7aae`](https://github.com/K-dash/flake8-import-guard/commit/bfa7aae0d287e8ac7bf1aa85521b3e49b2627ca0))

- Updated CI workflows and Makefile for uv usage, added uv setup, removed Poetry config and install
  steps
  ([`752be32`](https://github.com/K-dash/flake8-import-guard/commit/752be329363a0cabc8593362f2d4b01e747a2a12))

- Updated dependencies and python version requirements
  ([`6f05c47`](https://github.com/K-dash/flake8-import-guard/commit/6f05c470dbb0737a36956dd4801bca9ca198db84))

feat: Updated dependencies and Python version requirements

- Updated dependencies and Python version requirements
  ([`5eb95f2`](https://github.com/K-dash/flake8-import-guard/commit/5eb95f22bc7068332aeea9e64509d958040d30fe))

- Changed Python requirements in `pyproject.toml` to `>=3.9,<4 - Updated `flake8`, `python-dotenv`,
  `ruff`, `pytest` and `pytest-cov` versions to the latest respectively - Changed Python version of
  CI workflow from `3.8` to `3.9` to simplify test matrix

### Refactoring

- Improve syntax of `with` statement
  ([`44d7bbe`](https://github.com/K-dash/flake8-import-guard/commit/44d7bbe8defc6d5d1e8ea05079127b4627459d4d))

- The syntax of `with` statements with `patch` has been changed to improve readability. - The same
  changes have been applied to the `test_run_with_different_file_states`, `test_run_git_check`, and
  `test_run_git_command_fails` tests.


## v1.0.0 (2024-08-12)

### Bug Fixes

- Streamline forbidden import checks
  ([`c4e16b7`](https://github.com/K-dash/flake8-import-guard/commit/c4e16b7cfa5ebfddec39c9f2116db14945433e67))

### Features

- Add Dependabot configuration and auto-merge workflow
  ([`ad817c7`](https://github.com/K-dash/flake8-import-guard/commit/ad817c70767d514d6d4924f85fc762548f1eb08d))


## v0.1.6 (2024-07-31)

### Bug Fixes

- Upgrade flake8 to 7.1.0 for latest features and bug fixes
  ([`5d48a1c`](https://github.com/K-dash/flake8-import-guard/commit/5d48a1cd127ad135b9f3d348b4ecc46b21d98b59))


## v0.1.5 (2024-07-31)

### Bug Fixes

- **workflow**: Simplify test and coverage steps
  ([`00ee445`](https://github.com/K-dash/flake8-import-guard/commit/00ee4453b5e6b5dc46aec2785cd0b0ee300acb12))


## v0.1.4 (2024-07-30)


## v0.1.3 (2024-07-30)


## v0.1.2 (2024-07-30)


## v0.1.1 (2024-07-30)


## v0.1.0 (2024-07-30)

### Bug Fixes

- **workflows**: Trigger pipelines only on pull requests
  ([`49ca8ad`](https://github.com/K-dash/flake8-import-guard/commit/49ca8ad649370b6d210e461b477497126b7c266b))

### Features

- Add build and test workflows, update dependencies
  ([`4146f25`](https://github.com/K-dash/flake8-import-guard/commit/4146f25c3fd66a264c73a9bb56cbdcacf677b069))

- Add contributing guidelines and README for Flake8 Import Guard
  ([`ab99b22`](https://github.com/K-dash/flake8-import-guard/commit/ab99b2275808d2a7f0e4494ec966dd7036ca8ec2))

- Add Flake8 import guard plugin and update dependencies
  ([`61a3ad1`](https://github.com/K-dash/flake8-import-guard/commit/61a3ad1c02ee85d1685ae05a9ded0d4eb84dd8bb))

- Flake8プラグインを"flake8-import-guard"に変更し、新しい禁止インポートの構成を追加 -
  `poetry.lock`にて`gitpython`、`python-dotenv`、`toml`の新しい依存関係を追加 -
  `src/main.py`のリファクタリングを実施し、禁止インポートの検出ロジックを実装 - 新規および既存ファイルに対する禁止インポートの検証ロジックを追加 -
  `tests/test_code_pattern_enforcer.py`を削除し、`tests/test_main.py`を新規作成してテストケースを追加 -
  `.flake8`のローカルプラグイン設定を削除し簡略化

- Add GitHub Actions CI for linting and testing Python code
  ([`c3a5609`](https://github.com/K-dash/flake8-import-guard/commit/c3a5609b20de6263f6b9c85a0380ec0c46d52e78))

- Improve import guard and add Python 3.12 support
  ([`ea658a5`](https://github.com/K-dash/flake8-import-guard/commit/ea658a5e1816d49d87174ce04d5a4150d1e5e374))
