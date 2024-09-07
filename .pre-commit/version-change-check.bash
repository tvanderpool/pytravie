#!/bin/bash

# Check if the version has been changed in pyproject.toml
version_change=$(git diff HEAD -- pyproject.toml | grep '^+version' | cut -d'=' -f2 | sed 's|[" ]||g')

if [ -z "$version_change" ]; then
    echo "Version has not been changed in pyproject.toml"
    read -p "increment Version? blank to ignore: (m)inor, (r)evision, (s)top: " option

    case $option in
        mMrR)
            version=`grep '^+version' pyproject.toml | cut -d'=' -f2 | sed 's|[" ]||g'`
            version_parts=(${version//./ })
            major=${version_parts[0]}
            minor=${version_parts[1]}
            revision=${version_parts[2]}
            case $option in
                m|M) minor=$((minor + 1)) ;;
                r|R) revision=$((revision + 1)) ;;
            esac
            minor=$((minor + 1))
            new_version="$major.$minor.0"
            sed -i "s/^version = .*/version = \"$new_version\"/" pyproject.toml
            exit 1
            ;;
        sS) exit 1;;
        *) exit 0 ;;
    esac
else
    echo "Version has been changed to $version_change"
    exit 0
fi
