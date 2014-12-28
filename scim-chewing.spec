Summary:	Chewing Chinese input method for SCIM
Summary(pl.UTF-8):	Metoda wprowadzania znaków chińskich Chewing dla SCIM-a
Name:		scim-chewing
Version:	0.3.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://chewing.csie.net/download/scim/%{name}-%{version}.tar.bz2
# Source0-md5:	c37bd1e7198776117e68b7aa1060896d
Patch0:		%{name}-gtk3.patch
URL:		http://chewing.csie.net/
BuildRequires:	gettext-tools >= 0.14.1
BuildRequires:	intltool >= 0.34.0
BuildRequires:	libchewing-devel >= 0.3.3
BuildRequires:	libstdc++-devel
BuildRequires:	scim-devel >= 1.0.0
Requires:	libchewing >= 0.3.3
Requires:	scim >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Chewing Chinese input method for SCIM.

%description -l pl.UTF-8
Metoda wprowadzania znaków chińskich Chewing dla SCIM-a.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/chewing-imengine-setup.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/chewing.so
%{_datadir}/scim/icons/scim-chewing.png
%{_datadir}/scim/icons/scim-chewing-swap-colors.png
