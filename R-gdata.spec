%global packname  gdata
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}
%define __noautoreq 'perl.*'
%define __noautoprov 'perl.*'

Name:             R-%{packname}
Version:          2.13.2
Release:          1
Summary:          Various R programming tools for data manipulation
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/gdata_2.13.2.tar.gz
Requires:         R-gtools 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-gtools 

%description
Various R programming tools for data manipulation

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/perl
%{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/xls
