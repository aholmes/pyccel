# coding: utf-8

from pyccel.stdlib.parallel.mpi import mpi_init
from pyccel.stdlib.parallel.mpi import mpi_finalize
from pyccel.stdlib.parallel.mpi import mpi_comm_size
from pyccel.stdlib.parallel.mpi import mpi_comm_rank
from pyccel.stdlib.parallel.mpi import mpi_comm_world

ierr = -1
mpi_init(ierr)

comm = mpi_comm_world
print("comm = ", comm)

size = -1
mpi_comm_size(comm, size, ierr)
print("size = ", size)

rank = -1
mpi_comm_rank(comm, rank, ierr)
print("rank = ", rank)

##abort, ierr = mpi_abort(comm)
##print("mpi_abort = ", abort)

mpi_finalize(ierr)
