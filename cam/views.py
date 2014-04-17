from cam.scraper import download_all_past_exams
from flask import render_template, send_file, request
from cam import cam

ROOT = "http://www.maths.cam.ac.uk/postgrad/mathiii/pastpapers/"
YEARS = range(2001, 2014)

SUBJECTS = [
     u'Actuarial Statistics',
     u'Additive Combinatorics',
     u'Advanced Financial Models',
     u'Advanced Probability',
     u'Advanced Quantum Field Theory',
     u'Algebraic Geometry',
     u'Algebraic Number Theory',
     u'Algebraic Topology',
     u'Applications of Differential Geometry to Physics',
     u'Applied Bayesian Statistics',
     u'Applied Statistics',
     u'Approximation Theory',
     u'Aspects of Analysis',
     u'Astrophysical Fluid Dynamics',
     u'Binary Stars',
     u'Biological Physics',
     u'Biostatistics',
     u'Black Holes',
     u'Category Theory',
     u'Classical and Quantum Solitons',
     u'Combinatorics',
     u'Commutative Algebra',
     u'Complex Manifolds',
     u'Computability and Logic',
     u'Computational Complexity',
     u'Contemporary Sampling Techniques and Compressed Sensing',
     u'Convex Optimisation with Applications in Image Processing',
     u'Cosmology',
     u'Design of Experiments',
     u'Differential Geometry',
     u'Distribution Theory and Applications',
     u'Dynamics of Astrophysical Discs',
     u'Elliptic Curves',
     u'Extremal Graph Theory',
     u'Fluid Dynamics of Climate',
     u'Fluid Dynamics of Energy Systems',
     u'Fluid Dynamics of the Environment',
     u'General Relativity',
     u'Image Processing \u2014 Variational and PDE Methods',
     u'Introduction to Fourier Analysis',
     u'Lie Algebras and their Representations',
     u'Mathematics of Operational Research',
     u'Nonparametric Statistical Theory',
     u'Numerical Solution of Differential Equations',
     u'Optimal Investment',
     u'Origin and Evolution of Galaxies',
     u'Percolation and Related Topics',
     u'Perturbation and Stability Methods',
     u'Polar Oceans and Climate Change',
     u'Quantum Computation',
     u'Quantum Condensed Matter Field Theory',
     u'Quantum Field Theory',
     u'Quantum Foundations',
     u'Representation Theory',
     u'Schramm--Loewner Evolutions',
     u'Slow Viscous Flow',
     u'Solidification of Fluids',
     u'Sound Generation and Propagation',
     u'Spectral Geometry',
     u'Statistical Theory',
     u'Stochastic Calculus and Applications',
     u'Stochastic Networks',
     u'String Theory',
     u'Structure and Evolution of Stars',
     u'Supersymmetry',
     u'Symmetries, Fields and Particles',
     u'The Kakeya Universe and Incidence Problems in Rn',
     u'The Standard Model',
     u'Time Series and Monte Carlo Inference',
     u'Topics in Analytic Number Theory',
     u'Topics in Group Theory',
     u'Topics in Kinetic Theory',
     u'Topics in Set Theory',
     u'Topos Theory',
]


@cam.route('/', methods=['GET'])
def index():
    return render_template('index.html', subjects=SUBJECTS)

@cam.route("/", methods=['POST'])
def get_pdfs():
    subjects = request.form.getlist("do_download")
    print subjects
    cam.logger.info("Subjects: %s", subjects)
    return send_file(download_all_past_exams(YEARS, ROOT, subjects))
