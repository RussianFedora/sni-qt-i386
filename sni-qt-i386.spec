Summary:	Meta package to install 32-bit sni-qt
Name:		sni-qt-i386
Version:	0.0
Release:	1%{?dist}

License:	LGPLv3
URL:		https://github.com/RussianFedora/sni-qt-i386

Requires:	sni-qt(x86-32)

ExclusiveArch:	x86_64

%description
This package install 32-bit version of sni-qt. Should be used from
comps files.

%files

%changelog
* Wed Nov  4 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.0-1.R
- initial build
