Summary:	Polish resources for Mozilla
Summary(pl):	Polskie pliki jêzykowe dla Mozilli
Name:		mozilla-lang-pl
Version:	1.4
# use "a", "b", or "%{nil}"
%define	bver	b
%define	fver	%(echo %{bver} | sed -e 's/a/Alpha/;s/b/Beta/')
Release:	0.%{bver}.1
#Release:	1
License:        GPL
Group:          X11/Applications/Networking
Source0:	http://dl.sourceforge.net/mozillapl/Lang-PL-Build-ID-%{version}%{fver}.xpi
Source1:	http://dl.sourceforge.net/mozillapl/Reg-PL-Build-ID-%{version}%{fver}.xpi
Source2:	%{name}-installed-chrome.txt
URL:            http://mozillapl.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla = %{version}%{bver}
Requires(post,postun):	textutils
Requires:	mozilla = %{version}%{bver}
Obsoletes:	mozilla-Lang-PL
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# %{_libdir}/mozilla/chrome is symlink pointing to the following
%define         _chromedir      %{_datadir}/mozilla/chrome

%description
Polish resources for Mozilla.

%description -l pl
Polskie pliki jêzykowe dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_datadir}/mozilla/searchplugins}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
unzip -n %{SOURCE1} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/searchplugins/* \
	$RPM_BUILD_ROOT%{_datadir}/mozilla/searchplugins
# entries already in mozilla
rm -f $RPM_BUILD_ROOT%{_datadir}/mozilla/searchplugins/{Net,bug,dmoz,goo,lxr,moz}*

install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-unix.jar
%{_chromedir}/PL.jar
%{_chromedir}/%{name}-installed-chrome.txt
%{_datadir}/mozilla/searchplugins/*
