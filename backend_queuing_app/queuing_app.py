'''
backened (core functions)
'''
WAITING_LIST = []

def make_request(student_id, issue):
    '''
    Used by students to make a request. The request is put in the queue with a
    "waiting" status.
    Parameters:
      student_id (str): The student_id of the student making the request.

      issue (str): A brief issue of what the student needs help
      with.
    '''
    global WAITING_LIST

    if issue is None:
        raise ValueError
    if issue == "":
        raise ValueError
    # correspondoing student student_id is already insstudent_ide the queue.
    for student in WAITING_LIST:
        if student['student_id'] == student_id:
            raise KeyError

    WAITING_LIST.append({'student_id': student_id, 'issue': issue, 'status': 'waiting'})


def queue():
    '''
    Used by tutors to view all the students in the queue in order.

    Returns:
      (list of dict) : A list of dictionaries where each dictionary has the keys
      { 'student_id', 'issue', 'status' }. These correspond to the student's student_id,
      the issue of their problem, and the status of their request (either
      "waiting" or "receiving").
    '''
    global WAITING_LIST
    return WAITING_LIST

def remaining(student_id):
    '''
    Used by students to see how many requests there are ahead of theirs in the
    queue that also have a "waiting" status.

    Params:
      student_id (str): The student_id of the student with the request.

    Raises:
      KeyError: if the student does not have a request in the queue with a
      "waiting" status.

    Returns:
      (int) : The position as a number >= 0
    '''
    for student in queue():
        if student['student_id'] == student_id and student['status'] == 'receiving':
            raise KeyError
    for student in queue():
        if student['student_id'] == student_id:
            get_turn = queue().index(student)
            if queue()[0]['status'] == 'receiving':
                return get_turn - 1
    return get_turn

def help(student_id):
    '''
    Used by tutors to indicate that a student is getting help with their
    request. It sets the status of the request to "receiving".

    Params:
      student_id (str): The student_id of the student with the request.

    Raises:
      KeyError: if the given student does not have a request with a "waiting"
      status.
    '''
    for student in queue():
        if student['student_id'] == student_id:
            if student['status'] != 'waiting':
                raise KeyError
            student['status'] = 'receiving'

def resolve(student_id):
    '''
    Used by tutors to remove a request from the queue when it has been resolved.

    Params:
      student_id (str): The student_id of the student with the request.

    Raises:
      KeyError: if the given student does not have a request in the queue with a
      "receiving" status.
    '''
    for student in queue():
        if student['student_id'] == student_id:
            if student['student_id'] == student_id and student['status'] != 'receiving':
                raise KeyError
            queue().remove(student)
    # update student_id_TIME_PAIR dictionary because they've got help

def cancel(student_id):
    '''
    Used by students to remove their request from the queue in the event they
    solved the problem themselves before a tutor was a available to help them.

    Unlike resolve(), any requests that are cancelled are NOT counted towards
    the total number of requests the student has made in the session.

    Params:
      student_id (str): The student_id of the student who made the request.

    Raises:
      KeyError: If the student does not have a request in the queue with a
      "waiting" status.
    '''
    for student in queue():
        if student['student_id'] == student_id:
            if student['status'] != 'waiting':
                raise KeyError
            queue().remove(student)

def revert(student_id):
    '''
    Used by tutors in the event they cannot continuing helping the student. This
    function sets the status of student's request back to "waiting" so that
    another tutor can help them.

    Params:
      student_id (str): The student_id of the student with the request.

    Raises:
      KeyError: If the student does not have a request in the queue with a
      "receiving" status.
    '''
    for student in queue():
        if student['student_id'] == student_id:
            if student['status'] != 'receiving':
                raise KeyError
            student['status'] = 'waiting'

def reset_queue():
    '''
    Reset
    Used by tutors at the end of the help session. All requests are removed from
    the queue and any records of previously resolved requests are wiped.
    '''
    global WAITING_LIST
    WAITING_LIST = []
