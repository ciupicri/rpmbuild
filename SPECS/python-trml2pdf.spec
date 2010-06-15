%global srcname trml2pdf

Name:           python-trml2pdf
Version:        1.2
Release:        1%{?dist}
Summary:        Tiny RML2PDF is a tool to easily create PDF documents without programming

Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.satchmoproject.com/snapshots/
Source0:        http://www.satchmoproject.com/snapshots/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python2-devel
Requires:       python-reportlab >= 2.1
# Python-Imaging (PIL) if you use bitmap pictures
Requires:       python-imaging


%description
Convert Report Markup Language (RML) files to PDF.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# upsteam is a bit dead, so there's no one to extract a script from the module
chmod +x ${RPM_BUILD_ROOT}/%{python_sitelib}/trml2pdf/trml2pdf.py
install -m 755 -d ${RPM_BUILD_ROOT}/%{_bindir}
ln -s %{python_sitelib}/trml2pdf/trml2pdf.py ${RPM_BUILD_ROOT}/%{_bindir}/trml2pdf

 
%files
%defattr(-,root,root,-)
%doc COPYRIGHT.txt INSTALL.txt LICENSE.txt README.txt
%{python_sitelib}/*
%{_bindir}/trml2pdf


%changelog
* Mon Nov 08 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.2-1
- Initial package
