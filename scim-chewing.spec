Summary:	Chewing Chinese input method for SCIM
Name:		scim-chewing
Version:	0.3.4
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://chewing.csie.net/download/scim/%{name}-%{version}.tar.bz2
# Source0-md5:	c37bd1e7198776117e68b7aa1060896d
URL:		http://chewing.csie.net/
BuildRequires:	scim-devel
BuildRequires:	libchewing-devel >= 0.3.2
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Chewing Chinese input method for SCIM.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/chewing-imengine-setup.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/chewing.so
%{_datadir}/scim/icons/scim-chewing.png
%{_datadir}/scim/icons/scim-chewing-swap-colors.png
