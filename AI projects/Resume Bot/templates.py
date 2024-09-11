resumeTemplate = r"""
\documentclass[10pt, letterpaper]{article}

\usepackage[
    ignoreheadfoot, 
    top=2 cm, 
    bottom=2 cm, 
    left=2 cm, 
    right=2 cm, 
    footskip=1.0 cm, 
]{geometry} 
\usepackage{titlesec}
\usepackage{tabularx}
\usepackage{array}
\usepackage[dvipsnames]{xcolor} 
\definecolor{primaryColor}{RGB}{0, 0, 0}
\usepackage{enumitem} 
\usepackage{fontawesome5} 
\usepackage{amsmath} 
\usepackage[
    pdftitle={John Doe's CV},
    pdfauthor={John Doe},
    pdfcreator={LaTeX with RenderCV},
    colorlinks=true,
    urlcolor=primaryColor
]{hyperref} 
\usepackage[pscoord]{eso-pic} 
\usepackage{calc} 
\usepackage{bookmark} 
\usepackage{lastpage} 
\usepackage{changepage} 
\usepackage{paracol} 
\usepackage{ifthen} 
\usepackage{needspace} 
\usepackage{iftex} 

\ifPDFTeX
    \input{glyphtounicode}
    \pdfgentounicode=1
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage{lmodern}
\fi

\usepackage{charter}

\raggedright
\AtBeginEnvironment{adjustwidth}{\partopsep0pt} 
\pagestyle{empty} 
\setcounter{secnumdepth}{0}
\setlength{\parindent}{0pt}
\setlength{\topskip}{0pt} 
\setlength{\columnsep}{0.15cm}
\pagenumbering{gobble} 

\titleformat{\section}{\needspace{4\baselineskip}\bfseries\large}{}{0pt}{}[\vspace{1pt}\titlerule]

\titlespacing{\section}{
    -1pt
}{
    0.3 cm
}{
    0.2 cm
} 

\renewcommand\labelitemi{$\vcenter{\hbox{\small$\bullet$}}$} 
\newenvironment{highlights}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=0pt,
        leftmargin=0 cm + 10pt
    ]
}{
    \end{itemize}
} 


\newenvironment{highlightsforbulletentries}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=0pt,
        leftmargin=10pt
    ]
}{
    \end{itemize}
} 

\newenvironment{onecolentry}{
    \begin{adjustwidth}{
        0 cm + 0.00001 cm
    }{
        0 cm + 0.00001 cm
    }
}{
    \end{adjustwidth}
} 

\newenvironment{twocolentry}[2][]{
    \onecolentry
    \def\secondColumn{#2}
    \setcolumnwidth{\fill, 4.5 cm}
    \begin{paracol}{2}
}{
    \switchcolumn \raggedleft \secondColumn
    \end{paracol}
    \endonecolentry
} 

\newenvironment{threecolentry}[3][]{
    \onecolentry
    \def\thirdColumn{#3}
    \setcolumnwidth{, \fill, 4.5 cm}
    \begin{paracol}{3}
    {\raggedright #2} \switchcolumn
}{
    \switchcolumn \raggedleft \thirdColumn
    \end{paracol}
    \endonecolentry
} 

\newenvironment{header}{
    \setlength{\topsep}{0pt}\par\kern\topsep\centering\linespread{1.5}
}{
    \par\kern\topsep
} 

\newcommand{\placelastupdatedtext}{
  \AddToShipoutPictureFG*{
    \put(
        \LenToUnit{\paperwidth-2 cm-0 cm+0.05cm},
        \LenToUnit{\paperheight-1.0 cm}
    ){\vtop{{\null}\makebox[0pt][c]{
        \small\color{gray}\textit{Last updated in July 2024}\hspace{\widthof{Last updated in July 2024}}
    }}}
  }
}


\let\hrefWithoutArrow\href




\begin{document}
    \newcommand{\AND}{\unskip
        \cleaders\copy\ANDbox\hskip\wd\ANDbox
        \ignorespaces
    }
    \newsavebox\ANDbox
    \sbox\ANDbox{$|$}

    \begin{header}
        \fontsize{25 pt}{25 pt}\selectfont John Doe

        \vspace{5 pt}

        \normalsize
        \mbox{Your Location}
        \kern 5.0 pt
        \AND
        \kern 5.0 pt
        \mbox{\hrefWithoutArrow{mailto:youremail@yourdomain.com}{youremail@yourdomain.com}}
        \kern 5.0 pt
        \AND
        \kern 5.0 pt
        \mbox{\hrefWithoutArrow{tel:+90-541-999-99-99}{+90 541 999 99 99}}
        \kern 5.0 pt
        \AND
        \kern 5.0 pt
        \mbox{\hrefWithoutArrow{https://yourwebsite.com/}{yourwebsite.com}}
        \kern 5.0 pt
        \AND
        \kern 5.0 pt
        \mbox{\hrefWithoutArrow{https://linkedin.com/in/yourusername}{linkedin.com/in/yourusername}}
        \kern 5.0 pt
        \AND
        \kern 5.0 pt
        \mbox{\hrefWithoutArrow{https://github.com/yourusername}{github.com/yourusername}}
    \end{header}

    \vspace{5 pt - 0.3 cm}


    \section{Education}



        
        \begin{twocolentry}{
            Sept 2000 – May 2005
        }
            \textbf{University of Pennsylvania}, BS in Computer Science\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item GPA: 3.9/4.0 (\href{https://example.com}{Transcript})
                \item \textbf{Coursework:} Computer Architecture, Artificial Intelligence, Comparison of Learning Algorithms, Computational Theory
            \end{highlights}
        \end{onecolentry}



    
    \section{Experience}



        
        \begin{twocolentry}{
            June 2005 – Aug 2007
        }
            \textbf{Software Engineer}, Apple -- Cupertino, CA\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Reduced time to render the user's buddy list by 75\% by implementing a prediction algorithm
                \item Implemented iChat integration with OS X Spotlight Search by creating a tool to extract metadata from saved chat transcripts and provide metadata to a system-wide search database
                \item Redesigned chat file format and implemented backward compatibility for search
            \end{highlights}
        \end{onecolentry}


        \vspace{0.2 cm}

        \begin{twocolentry}{
            Sept 2003 – Apr 2005
        }
            \textbf{Lead Student Ambassador}, Microsoft -- Redmond, WA\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Promoted to Lead Student Ambassador in the Fall of 2004, supervised 10-15 Student Ambassadors
                \item Created and taught a computer science course, CSE 099: Software Design and Development
            \end{highlights}
        \end{onecolentry}


        \vspace{0.2 cm}

        \begin{twocolentry}{
            Oct 2001 – May 2003
        }
            \textbf{Head Teaching Assistant}, University of Pennsylvania -- Philadelphia, PA\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Implemented a user interface for the VS open file switcher (ctrl-tab) and extended it to tool windows
                \item Created a service to provide gradient across VS and VS add-ins, optimized its performance via caching
                \item Programmer Productivity Research Center (Summers 2001, 2002)
                \item Built an app to compute the similarity of all methods in a code base, reducing the time from $\mathcal{O}(n^2)$ to $\mathcal{O}(n \log n)$
                \item Created a test case generation tool that creates random XML docs from XML Schema
            \end{highlights}
        \end{onecolentry}


        \vspace{0.2 cm}

        \begin{twocolentry}{
            June 2003 – Aug 2003
        }
            \textbf{Software Engineer, Intern}, Microsoft -- Redmond, WA\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Automated the extraction and processing of large datasets from legacy systems using SQL and Perl scripts
            \end{highlights}
        \end{onecolentry}



    
    \section{Publications}



        
        \begin{samepage}
            \begin{twocolentry}{
                Jan 2004
            }
                \textbf{Magneto-Thermal Thin Shell Approximation for 3D Finite Element Analysis of No-Insulation Coils}
            \end{twocolentry}

            \vspace{0.10 cm}
            
            \begin{onecolentry}
                \mbox{Albert Smith}, \mbox{\textbf{\textit{John Doe}}}, \mbox{Jane Derry}, \mbox{Harry Tom}, \mbox{Frodo Baggins}

                \vspace{0.10 cm}
                
        \href{https://doi.org/10.1109/TASC.2023.3340648}{10.1109/TASC.2023.3340648}
        \end{onecolentry}
        \end{samepage}

    \section{Projects}
        
        \begin{twocolentry}{
            \href{https://github.com/sinaatalay/rendercv}{github.com/name/repo}
        }
            \textbf{Multi-User Drawing Tool}\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Developed an electronic classroom where multiple users can view and simultaneously draw on a "chalkboard" with each person's edits synchronized
                \item Tools Used: C++, MFC
            \end{highlights}
        \end{onecolentry}


        \vspace{0.2 cm}

        \begin{twocolentry}{
            \href{https://github.com/sinaatalay/rendercv}{github.com/name/repo}
        }
            \textbf{Synchronized Calendar}\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Developed a desktop calendar with globally shared and synchronized calendars, allowing users to schedule meetings with other users
                \item Tools Used: C\#, .NET, SQL, XML
            \end{highlights}
        \end{onecolentry}


        \vspace{0.2 cm}

        \begin{twocolentry}{
            2002
        }
            \textbf{Operating System}\end{twocolentry}

        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Developed a UNIX-style OS with a scheduler, file system, text editor, and calculator
                \item Tools Used: C
            \end{highlights}
        \end{onecolentry}

    \section{Additional Experience And Awards}

        \begin{onecolentry}
            \textbf{Instructor (2003-2005):} Taught 2 full-credit computer science courses
        \end{onecolentry}

        \vspace{0.2 cm}

        \begin{onecolentry}
            \textbf{Third Prize, Senior Design Project:} Awarded 3rd prize for a synchronized calendar project out of 100 entries
        \end{onecolentry}

    \section{Technologies}
        \begin{onecolentry}
            \textbf{Languages:} C++, C, Java, Objective-C, C\#, SQL, JavaScript
        \end{onecolentry}

        \vspace{0.2 cm}

        \begin{onecolentry}
            \textbf{Software:} .NET, Microsoft SQL Server, XCode, Interface Builder
        \end{onecolentry}
\end{document}

"""