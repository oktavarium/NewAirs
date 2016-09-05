
function sign(val) {
    //

    if (val < 0) return -1;
    else return 1;
}

function line(object, x_pos, y_pos, angle, coef) {
    //

    if (x_pos === undefined) x_pos = 0;
    if (y_pos === undefined) y_pos = 0;
    if (angle === undefined) angle = 0;
    if (coef === undefined) coef = 1;

    angle %= 360;
    var angle_rad = angle * (Math.PI / 180);
    var _tg = Math.tan(angle_rad);

    // define area's width & height
    if (object === 0 || typeof(object) === undefined) object = window;

    var _width = object.offsetWidth;
    var _height = object.offsetHeight;

    var x_orig = 0; // object.offsetLeft;
    var y_orig = 0; // object.offsetTop;

    var x_to = 0;
    var y_to = 0;

    if (angle <= 90 || (angle > 270 && angle <= 360)) {
        //

        y_orig = 0;

    } else if (angle > 90 && angle <= 270) {
        //

        y_orig = _height;
    }

    var y_df = (y_pos - y_orig);
    var x_df = Math.abs(_width - x_pos);

    var x_add = _tg * y_df;

    x_to = x_pos + x_add;
    y_to = y_orig;

    var CObj = {x_pos: x_pos, y_pos: y_pos, x_to: x_to, y_to: y_to};
    return CObj;
}
