package com.worldsensing.innovation.testing.ws_test;

import android.support.test.filters.SmallTest;
import android.support.test.runner.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.assertEquals;

/**
 * Instrumented test, which will execute on an Android device.
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
@RunWith(AndroidJUnit4.class)
@SmallTest
public class ExampleJUnit4InstrumentedSmallTest {
    @Test
    public void addition_isCorrect() {
        assertEquals(4, 2 + 2);
    }
}