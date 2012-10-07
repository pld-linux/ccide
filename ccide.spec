Summary:	C Language Decision Table Code Generator
Summary(pl.UTF-8):	Generator kodu tablic decyzyjnych w języku C
Name:		ccide
Version:	0.6.6
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/ccide/%{name}-%{version}.tar.gz
# Source0-md5:	fdbc8822b1d79ebc56939d47b36244c6
URL:		http://ccide.sourceforge.net/
BuildRequires:	gettext-devel >= 0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C Language Decision Table Code Generator.

%description -l pl.UTF-8
Generator kodu tablic decyzyjnych w języku C.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ccide
%attr(755,root,root) %{_bindir}/ccidew
%{_datadir}/ccide
%{_mandir}/man1/ccide.1*
